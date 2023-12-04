import sys
import time
start_time = time.time()

spelled_numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def find_number (line, sequence):
    for i in sequence:
        if line[i].isdigit():
            return line[i]
        else:
            for word, num in spelled_numbers.items():
                if line[i:].startswith(word):
                    return num

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

numbers = [int(find_number(line, range(len(line))) + find_number(line, reversed(range(len(line))))) for line in lines]
print(sum(numbers))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
