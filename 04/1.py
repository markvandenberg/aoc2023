import sys
import time
start_time = time.time()


with open(sys.argv[1]) as text_file:
    lines = text_file.read().splitlines()

total = 0
score = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

cards = [([int(x) for x in z[0].split(': ')[1].split()], [int(x) for x in z[1].split()]) for z in [y.split(' | ') for y in lines]]

print(sum([score[len(winning)] for winning in [set(winners).intersection(numbers) for winners, numbers in cards]]))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
