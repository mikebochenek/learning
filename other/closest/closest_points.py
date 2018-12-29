from struct import *
from datetime import datetime

class Point:
    def __init__(self, x,  y,  d):
        self.x = x
        self.y = y
        self.d = d
    def __repr__(self):
        return repr((self.x, self.y))

f = open("/home/mike/Downloads-1/points", "rb")
try:
    bytes_read = f.read()
    idx = 0;
    list = []
    for b in bytes_read[0::4]:
        x = unpack('>h',  bytes_read[idx:idx+2])
        y = unpack('>h',  bytes_read[idx+2:idx+4])
        idx += 4
        p = Point(x[0], y[0],  0)
        list.append(p) 
finally:
    f.close()

def find(list,  target,  first,  closest):
    sampleDistances = []
    for l in list[0::1000]:
        xd = target.x - l.x
        yd = target.y - l.y
        d = xd * xd + yd * yd
        sampleDistances.append(d)
    min = sorted(sampleDistances)[first]
    max = sorted(sampleDistances,  reverse=True)[first]
    
    relevantPoints = []
    for l in list:
        xd = target.x - l.x
        yd = target.y - l.y
        l.d = xd * xd + yd * yd
        if (closest & l.d < min):
            relevantPoints.append(l)
        if (closest == False & l.d > max):
            relevantPoints.append(l)

    if (closest):
        result = sorted(relevantPoints, key=lambda point: point.d)
    else:
        result = sorted(relevantPoints, key=lambda point: point.d,  reverse=True)
    
    for r in result[0:first:]:
        print(r)
        
    return
    
start = datetime.now()
find(list,  Point(-200, 300,  0),  10,  True)
print(datetime.now() - start)

print ("\n")
start = datetime.now()
find(list,  Point(1000, 25,  0),  20,  False)
print(datetime.now() - start)
