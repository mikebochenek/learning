# https://stackabuse.com/read-a-file-line-by-line-in-python/
# https://docs.python-guide.org/writing/style/
from datetime import datetime

def testreadcsv(filename):
    startTime = datetime.now()

    count = 0
    with open('/Users/mike/Downloads/' + filename + '.csv') as f:
        for line in f:
            count = count + len(line)
            #len(line)
            #print (line, end=' ')  # Do something with 'line'

    print(datetime.now() - startTime, 'time taken to read small csv ', count, filename) 

testreadcsv('WIR100OD1007') # https://data.stadt-zuerich.ch/dataset/fd_median_einkommen_kreis_od1007/download/WIR100OD1007.csv
testreadcsv('10210') # https://data.bl.ch/api/v2/catalog/datasets/10210/exports/csv