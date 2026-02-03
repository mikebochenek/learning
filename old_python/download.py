import urllib2
from datetime import datetime

# http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
start = datetime.now().microsecond

# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
mp3file = urllib2.urlopen("http://upload.wikimedia.org/wikipedia/commons/2/21/ZurichMontage.jpg")
output = open('/tmp/Zurich.jpg','wb')
output.write(mp3file.read())
output.close()

end = datetime.now().microsecond
print str(end - start)

# or alternatively
# http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python
# import urllib
# testfile = urllib.URLopener()
# testfile.retrieve("http://randomsite.com/file.gz", "file.gz")

