# Script to easily count pattern in genome

import sys

# main program
if __name__ == "__main__":
    pattern = str(sys.stdin.readlines(1))
    genome = str(sys.stdin.readlines(1))

    pattern = pattern[2:len(pattern) - 4]
    genome = genome[2:len(genome) - 4]
    count = 0
    k = 0
    for i in range(0, len(genome)):
        k = i
        for j in range(0, len(pattern)):
            if (k >= len(genome)):
                break
            if (genome[k] != pattern[j]):
                break
            else:
                k += 1
                if (j == len(pattern) - 1):
                    count += 1
                    break
    print(count)