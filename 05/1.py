import sys
import time
start_time = time.time()

with open(sys.argv[1]) as text_file:
    data = text_file.read().split('\n\n')

    seeds = [int(seed) for seed in data[0].split(': ')[1].split()]
    maps = [[[int(num) for num in row.split()] for row in map.split(':\n')[1].split('\n')] for map in data[1:]]
    locations = seeds.copy()
    
    for i, seed in enumerate(seeds):
        location = seed
        for map in maps:
            for destination, source, lenght in map:
                if location in range(source, source + lenght):
                    location = location + destination - source
                    break
        locations[i] = location

print(min(locations))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
