import re
# start Wed Dec  6 20:21:32 CET 2023 - Wed Dec  6 21:59:10 CET 2023
def perms(ts, ds):
    total = 1

    for idx in range(0, len(ts)):
        count = 0

        # to be optimized
#        for i in range(0, ts[idx]):
#            d = (ts[idx] - i) * i
#            if d > ds[idx]:
#                count += 1
            #print (' ', d, ts[idx])
        # print (ts[idx], ds[idx], ' -> ', count)

        i = 0
        _min = ds[idx]
        while (_min >= ds[idx]):
            if (ts[idx] - i) * i > ds[idx]:
                _min = i 
            else:
                i += 1

        i = 0
        _max = ds[idx]
        while (_max >= ds[idx]):
            if (ts[idx] - i) * i > ds[idx]:
                _max = ts[idx] - i
            else:
                i += 1

        nc = _max - _min + 1
        #print (_min, _max)

        print (ds[idx], 'time', ts[idx], count, '?=', nc, count == nc)

        total = total * count

    #print(ts,ds)

    return total


#Time:      7  15   30
#Distance:  9  40  200
print(288 == perms([7,15,30], [9,40,200]))

#Time:        63     78     94     68
#Distance:   411   1274   2047   1035
print(781200 == perms([63,78,94,68], [411,1274,2047,1035]))

# part I done at 20:35 ! 

print(71503 == perms([71530], [940200]))

# print(perms([63789468], [411127420471035]))
# 411127420471035 time 63789468 0 ?= 49240091 False
