import re

# start Wed Dec  6 20:21:32 CET 2023

def perms(ts, ds):
    total = 1

    for idx in range(0, len(ts)):
        count = 0
        for i in range(0, ts[idx]):
            d = (ts[idx] - i) * i
            if d > ds[idx]:
                count += 1
            #print (' ', d, ts[idx])
        # print (ts[idx], ds[idx], ' -> ', count)
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
