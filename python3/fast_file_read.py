# https://stackabuse.com/read-a-file-line-by-line-in-python/
# https://docs.python-guide.org/writing/style/
from datetime import datetime
import os.path
import urllib.request

files = {'WIR100OD1007': 'https://data.stadt-zuerich.ch/dataset/fd_median_einkommen_kreis_od1007/download/WIR100OD1007.csv', 
         '10210': 'https://data.bl.ch/api/v2/catalog/datasets/10210/exports/csv'}

def testreadcsv(filename):
    startTime = datetime.now()

    count = 0
    fullpath = '/Users/mike/Downloads/' + filename + '.csv'
    if (os.path.isfile(fullpath) == False):
        print ('lets download it then')
        urllib.request.urlretrieve(files.get(filename), fullpath)
        # urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>
    else:
        print ('already exists', fullpath)

    with open(fullpath) as f:
        for line in f:
            count = count + len(line)
            #len(line)
            #print (line, end=' ')  # Do something with 'line'

    print(datetime.now() - startTime, 'time taken to read small csv ', count, filename) 

for key, value in sorted(files.items()):
    testreadcsv(key) # 
