import sys
import time
start_time = time.time()

# met dank aan kanta
def find_in_maps(ranges, maps, i=0):
    if i >= len(maps):
        return min([x.start for x in ranges])

    next_ranges = []
    remaining_r = ranges

    for source_r, dest_r in maps[i]:

        new_remaining_r = []

        for current_r in remaining_r:
            if current_r.start <= source_r.stop and current_r.stop >= source_r.start:
                overlap = range(max(current_r.start, source_r.start), min(current_r.stop, source_r.stop))
                next_ranges.append(range(
                    overlap.start + dest_r.start - source_r.start,
                    overlap.stop + dest_r.stop - source_r.stop
                ))

                # get above range
                if overlap.stop < current_r.stop:
                    new_remaining_r.append(range(overlap.stop, current_r.stop))

                # get under range
                if overlap.start > current_r.start:
                    new_remaining_r.append(range(current_r.start, overlap.start))
            else:
                new_remaining_r.append(current_r)

        remaining_r = new_remaining_r

    next_ranges += remaining_r

    return find_in_maps(next_ranges, maps, i + 1)

with open(sys.argv[1]) as text_file:
    data = text_file.read().split('\n\n')
    seed_data = [int(seed) for seed in data[0].split(': ')[1].split()]
    seed_ranges = [[start, start + num] for start, num in list(zip(seed_data[::2], seed_data[1::2]))]
    maps = [[[int(num) for num in row.split()] for row in map.split(':\n')[1].split('\n')] for map in data[1:]]
    maps_ranges = [[[range(source, source + lenght), range(dest, dest + lenght)] for dest, source, lenght in map] for map in maps]

    results = []
    for start, end in seed_ranges:
        results.append(find_in_maps([range(start, end)], maps_ranges))

    print(min(results))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
