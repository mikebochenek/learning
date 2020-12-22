# https://adventofcode.com/2020/day/9  --- Day 9: Encoding Error ---
print ('starting day #9 (after skipping some days)...')

#with open('data/day9-test.txt') as f:
with open('data/day9.txt') as f:
    lines = f.read().splitlines()

preamble = 25 #5
numbers = []
notfound = 0
for l in lines:
    numbers.append(int(l))

for k in range (len(numbers)):
    found = False
    #print ('--------\n', k)
    for idx, n in enumerate(numbers):
        if idx < (preamble+k) and idx >= k:
            for i, x in enumerate(numbers):
                if i < (preamble+k) and i >= k  and idx != i:
                    #print ('   trying:', n, '+', x, '=', n+x)
                    if (k+preamble < len(numbers) and n+x == numbers[k+preamble]):
                        found = True
                        #print ((k+preamble), numbers[k+preamble], n, x, 'sums to:', (n+x))
    if (found == False and k+preamble < len(numbers)):
        print (' ------- not found:', (k+preamble), numbers[k+preamble])
        notfound = numbers[k+preamble]
print (numbers)

print ('\n\n------------part 2---------\n\n')

for i, x in enumerate(numbers):
    total = x
    for j, y in enumerate(numbers):
        if j > i:
            #print(i,j)
            total += y
            if (total == notfound):
                print (i,j,x,y)
                sublist = numbers[i:j+1]
                sublist.sort()
                print (sublist)
                smallest = sublist[0]
                largest = sublist[len(sublist)-1]
                print (smallest, largest, 'gives our final answer:', smallest+largest)
# 675280050