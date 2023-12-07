import sys
import time
start_time = time.time()

with open(sys.argv[1]) as text_file:
    lines = text_file.read().splitlines()

cards = [([int(x) for x in z[0].split(': ')[1].split()], [int(x) for x in z[1].split()]) for z in [y.split(' | ') for y in lines]]
score = {key: 1 for key in range(len(cards))} 

for index, (winning, card) in enumerate(cards):
    wins = len(list(set(winning).intersection(card)))
    
    for copies in range(1, wins + 1):
        if index + copies <= len(cards):
            score[index + copies] += 1 * score[index]

print(sum(score.values()))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
