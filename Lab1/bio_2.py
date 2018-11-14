# Script to easily count pattern in genome

import sys

# main program
if __name__ == "__main__":
    text = str(sys.stdin.readlines(1))
    k = str(sys.stdin.readlines(1))

    text = text[2:len(text) - 4]
    k = str(k[2:len(k) - 4])
    print(k)
    k = int(k)
    count = set()
    res = dict()
    set_uniq = set()
    for i in range(0, len(text)):
        pattern = text[i:i + k]
        if (pattern in set_uniq):
            if pattern in count:
                res[f'{pattern}'] += 1
            else:
                res[f"{pattern}"] = 2
                count.add(pattern)
        else:
            set_uniq.add(pattern)
    find_max = res.values()
    f = max(find_max)
    for key in res:
        if res[key] == f:
            print(key)