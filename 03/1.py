import sys
import time
import numpy as np
start_time = time.time()


with open(sys.argv[1]) as text_file:
    lines = text_file.read().splitlines()

x_len = len(lines[0])

data = np.array(list(''.join(lines)))
last_p = len(data) - 1

total = 0
num = ""

for p in range(len(data)):

    if data[p].isnumeric():
        num += data[p]
    
    if (not data[p].isnumeric() and num != "") or (p == last_p and data[p].isnumeric()):

        above = list(range(max(0, p - len(num) - 1 - x_len), max(0, p - x_len + 1)))
        front = [ p - len(num) - 1] if p - len(num) - 1 > 0 else []
        back = [p] if p < last_p else []
        below = list(range(min(p - len(num) - 1 + x_len, last_p), min(p + x_len + 1, last_p + 1)))
        
        if np.any([not c.isnumeric() and c != '.' for c in np.take(data, above + front + back + below)]):
            total += int(num)

        num = ""

print(total)

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
