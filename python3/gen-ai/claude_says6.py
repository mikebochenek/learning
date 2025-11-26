# https://claude.ai/chat/b0507112-6676-4ac9-8aa9-4468a2eade38
import os
import requests
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time

class WebsiteScraper:
    def __init__(self, start_url, output_dir="website_backup"):
        self.start_url = start_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.domain = urlparse(start_url).netloc
        
        Path(self.output_dir).mkdir(exist_ok=True) # Create output directory
    
    def is_same_domain(self, url): # Check if URL belongs to the same domain
        return urlparse(url).netloc == self.domain
    
    def normalize_url(self, url): #Remove fragments and query parameters for consistency
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    
    def get_local_path(self, url): # Convert URL to local file path
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')
        
        if not path or path.endswith('/'): # If it's just a domain, save as index.html
            path = os.path.join(path, 'index.html')
        
        local_path = os.path.join(self.output_dir, path)
        return local_path
    
    def download_file(self, url, local_path): #Download a file and save it locally
        try:
            resp = requests.get(url, timeout=10, allow_redirects=True)
            resp.raise_for_status()
            
            # Create directories if needed
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            with open(local_path, 'wb') as f:
                f.write(resp.content)  # Save the file
            
            print(f"✓ Downloaded: {url}")
            return resp.text, resp.headers.get('content-type', '')
        except requests.RequestException as e:
            print(f"✗ Error downloading {url}: {e}")
            return None, None
    
    def extract_links(self, html, base_url): # Extract all links from HTML content
        from html.parser import HTMLParser
        links = []
        
        class LinkParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                if tag == 'a':
                    for attr, value in attrs:
                        if attr == 'href' and value:
                            links.append(value)
        
        try:
            parser = LinkParser()
            parser.feed(html)
        except:
            pass
        
        # Convert relative URLs to absolute
        absolute_links = [urljoin(base_url, link) for link in links]
        return absolute_links
    
    def scrape(self, url=None): # Recursively scrape the website
        if url is None:
            url = self.start_url
        
        normalized_url = self.normalize_url(url) # Normalize and check if already visited
        if normalized_url in self.visited_urls:
            return
        
        self.visited_urls.add(normalized_url)
        
        if not self.is_same_domain(url): # Only scrape same domain
            print(f"⊘ Skipping external URL: {url}")
            return
        
        local_path = self.get_local_path(url) # Download the page
        html, content_type = self.download_file(url, local_path)
        
        if html is None:
            return
        
        # If it's HTML, extract and follow links
        if 'text/html' in content_type or url.endswith('.html') or url.endswith('/'):
            links = self.extract_links(html, url)
            
            for link in links:
                normalized_link = self.normalize_url(link)
                if normalized_link not in self.visited_urls and self.is_same_domain(link):
                    time.sleep(0.5)  # Be respectful with requests
                    self.scrape(link)
        
        print(f"Visited {len(self.visited_urls)} pages so far...")

if __name__ == "__main__":
    # Configure these:
    WEBSITE_URL = "https://mastodo.ch/"  # Change to your website
    OUTPUT_DIR = "c:\\dev\\data\\mastodo.ch"         # Where to save files
    
    scraper = WebsiteScraper(WEBSITE_URL, OUTPUT_DIR)
    print(f"Starting to scrape {WEBSITE_URL}...")
    scraper.scrape()
    print(f"\n✓ Complete! Website saved to {OUTPUT_DIR}/")