# Parsing - Extract and analyze
text = "Hello, World! 123"
print(f"Characters: {list(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Count of 'o': {text.count('o')}")

# Reversal - Flip it around
print(f"\nReversed: {text[::-1]}")
print(f"Words reversed: {' '.join(text.split()[::-1])}")

# Splitting - Break it apart
words = text.split()
print(f"\nWords: {words}")
print(f"First word: {words[0]}, Last word: {words[-1]}")

# Slicing - Extract substrings
print(f"\nFirst 5 chars: {text[:5]}")
print(f"Last 3 chars: {text[-3:]}")
print(f"Every 2nd char: {text[::2]}")

# Replacement - Transform
print(f"\nReplace 'World' with 'Python': {text.replace('World', 'Python')}")
print(f"Remove numbers: {text.translate(str.maketrans('', '', '0123456789'))}")

# Searching - Find things
print(f"\nContains 'World': {'World' in text}")
print(f"Index of 'World': {text.find('World')}")
print(f"Starts with 'Hello': {text.startswith('Hello')}")

# Try running this and experimenting by changing the text variable to different strings. 
# The slicing syntax [start:end:step] is particularly powerful—[::-1] reverses, 
# [::2] takes every other character, and [5:10] grabs characters 5-9. Have fun exploring!