# https://stackabuse.com/read-a-file-line-by-line-in-python/

with open('/Users/mike/Downloads/travel-types-data.csv') as f:
    for line in f:
        print (line, end=' ')  # Do something with 'line'
        
# also see: https://docs.python-guide.org/writing/style/
