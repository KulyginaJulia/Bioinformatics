# Script to easily count pattern in genome

import sys

def reverse(char):
    if char == "A":
        return "T"
    if char == "T":
        return "A"
    if char == "G":
        return "C"
    if char == "C":
        return "G"

# main program
if __name__ == "__main__":
    text = str(sys.stdin.readlines(1))
    text = text[2:len(text) - 2]
    reverse_str = ""
    for char in text:
        reverse_str += reverse(char)

    result = reverse_str[::-1]
    print(result)