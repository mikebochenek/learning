import pandas as pd
import re

def read_google_sheet(sheet_url, sheet_name=0):
    """
    Read data from a publicly shared Google Sheet and return as a pandas DataFrame.
    
    Parameters:
    -----------
    sheet_url : str
        The shareable URL of the Google Sheet (e.g., https://docs.google.com/spreadsheets/d/...)
    sheet_name : int or str, optional
        Sheet name or index to read (default: 0, reads first sheet)
    
    Returns:
    --------
    pd.DataFrame
        DataFrame containing the sheet data
    
    Example:
    --------
    >>> url = "https://docs.google.com/spreadsheets/d/1mHIWnDvW9cABJiRg6Sc7l1K3Dj6-3Y0X0Q0Q0Q0Q0Q/edit"
    >>> df = read_google_sheet(url)
    """
    
    # Extract the spreadsheet ID from the URL
    match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', sheet_url)
    if not match:
        raise ValueError("Invalid Google Sheets URL format")
    
    spreadsheet_id = match.group(1)
    
    # XLSX export lets pandas select a worksheet by name or index.
    export_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=xlsx"
    df = pd.read_excel(export_url, sheet_name=sheet_name)
    
    return df


# Example usage
if __name__ == "__main__":
    # Replace with your actual Google Sheet URL
    sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit"
    
    try:
        df = read_google_sheet(sheet_url)
        print("Data successfully loaded!")
        print(df.head())
    except Exception as e:
        print(f"Error: {e}")