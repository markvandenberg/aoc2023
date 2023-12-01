import sys
import time
start_time = time.time()

with open(sys.argv[1]) as text_file:
    lines = text_file.read().split('\n')

digits = [[i for i in x if i.isdigit()] for x in lines]
numbers = [int(digit[0] + digit[-1]) for digit in digits]
print(sum(numbers))
    
print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
