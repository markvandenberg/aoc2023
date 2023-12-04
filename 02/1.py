import sys
import time
start_time = time.time()

with open(sys.argv[1]) as text_file:
    lines = text_file.read().splitlines()

ids = [int(title.split()[1]) for title in [line.split(': ')[0] for line in lines]]

cubes = [[z.split(', ') for z in x.split('; ')] for x in [y.split(': ')[1] for y in lines]]    
cubes = [[[draw.split() for draw in set.split(', ')] for set in game.split('; ')] for game in [line.split(': ')[1] for line in lines]]
games = dict(zip(ids, cubes))

total = 0
lim_blue = 14
lim_green = 13
lim_red = 12

# Iterate through each game and count the occurrences of red
for key, game in games.items():

    impossible = False
    for set in game:
        for count, color in set:
            if color == 'red' and int(count) > lim_red:
                impossible = True
            elif color == 'blue' and int(count) > lim_blue:
                impossible = True
            elif color == 'green' and int(count) > lim_green:
                impossible = True

    if not impossible:
        total += key

print(total)

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
