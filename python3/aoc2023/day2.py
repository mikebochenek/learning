def sum_possible(filename):

    max_red = 12
    max_green = 13
    max_blue = 14

    with open('/Users/mike/Documents/aoc2023/'+filename+'.txt') as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        game_num = int(line.split(':')[0].split(' ')[1])
        games = line.split(':')[1].split(';')
        #print(len(games))
        possible = True
        min_red = 0
        min_green = 0
        min_blue = 0
        for game in games:
            counts = game.split(',')

            for count in counts:

                c = int(count.split(' ')[1])
                color = count.split(' ')[2]
                if ((color == 'red' and c <= max_red) 
                    or (color == 'green' and c <= max_green)
                    or (color == 'blue' and c <= max_blue)):
                    #print('possible', count)
                    None
                else:
                    possible = False
                    #print('not possible', c, color)

                if (color == 'red' and c > min_red):
                    min_red = c
                if (color == 'green' and c > min_green):
                    min_green = c
                if (color == 'blue' and c > min_blue):
                    min_blue = c

        power = min_red * min_green * min_blue
        #print('done', min_red, min_green, min_blue, power)

        #if possible:
        total = total + power #game_num
    
    print('total possible', total)
    return total

print(sum_possible('day2-0') == 8)
print(sum_possible('day2-1'))   # part two took < 40 mins (08:48 to approx. 09:25)