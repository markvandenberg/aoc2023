import sys
import time
import numpy as np
start_time = time.time()

with open(sys.argv[1]) as text_file:
    data = text_file.read().splitlines()

    times = int(data[0].split('Time: ')[1].replace(' ', ''))
    distances = int(data[1].split('Distance: ')[1].replace(' ', ''))
    races = [[times, distances]]
    
    print(np.prod([len([r for r in range(t) if r * (t - r) > d]) for t, d in races]))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
