# run with: [ Sat May 23 16:01:59 ~/Dev/spark-1.0.2-bin-hadoop2/bin ] ./pyspark ~/Dev/learning/python/SimpleApp.py

from pyspark import SparkContext

logFile = "/var/log/udev"
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
