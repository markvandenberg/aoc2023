import sys
import time
import numpy as np
import pandas as pd

start_time = time.time()

with open(sys.argv[1]) as text_file:
    lines = text_file.read().splitlines()

x_len = len(lines[0])

data = np.array(list(''.join(lines)))
last_p = len(data) - 1

total = 0
num = ""
gear_part = []

for p in range(len(data)):
    if data[p].isnumeric():
        num += data[p]
    
    if (not data[p].isnumeric() and num != "") or (p == last_p and data[p].isnumeric()):

        above = list(range(max(0, p - len(num) - 1 - x_len), max(0, p - x_len + 1)))
        front = [ p - len(num) - 1] if p - len(num) - 1 > 0 else []
        back = [p] if p < last_p else []
        below = list(range(min(p - len(num) - 1 + x_len, last_p), min(p + x_len + 1, last_p + 1)))

        junktions = [i for i in above + front + back + below if data[i] == '*']
        
        for j in junktions:
            gear_part.append([j, int(num)])

        num = ""

df = pd.DataFrame(gear_part, columns=['join', 'num']).sort_values('join')
gears = pd.merge(df.iloc[::2], df.iloc[1::2], on='join')

print((gears['num_x'] * gears['num_y']).sum())

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
