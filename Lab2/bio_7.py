# Script to easily count pattern in genome

import sys
Mass_table = {'G' : 57,
               'A' : 71,
               'S' : 87,
               'P' : 97,
               'V' : 99,
               'T' : 101,
               'C' : 103,
               'I' : 113,
               'L' : 113,
               'N' : 114,
               'D' : 115,
               'K' : 128,
               'Q' : 128,
               'E' : 129,
               'M' : 131,
               'H' : 137,
               'F' : 147,
               'R' : 156,
               'Y' : 163,
               'W' : 186
               }

#def recurse(mass_text, num, string, str2):
#    if num == len(mass_text):
#        str2[string] = num
#        return
#    recurse(mass_text, num + 1, string, str2)
#    string += str(mass_text[num])
#    recurse(mass_text, num + 1, string, str2)

def prohod(mass, text, num):
    i = 0
    while i < len(text):
        if (i + num > len(text)):
            free = len(text) - i
            second = num - free
            string_tmp = text[i:len(text)]
            string_tmp += text[0:second]
            mass.append(string_tmp)
        else:
            mass.append(text[i:i+num])
        i += 1
    return mass
# main program
if __name__ == "__main__":
    text = str(sys.stdin.readlines(1))
    text = text[2:len(text) - 4]
    #mass_text = []
    #for char in text:
    #    mass_text.extend(char)
    #str2 = {}
    #res_str = []
    #recurse(mass_text, 0, "", str2)
    #res_str = list(str2.keys())
    res_mas = []
    #for chars in res_str:
    #    if char == '':
    #        res_mas.append(0)
    #    else:
    #        tmp = 0
    #        i = 0
    #        while i < len(chars):
    #            tmp += Mass_table[chars[i]]
    #            i += 1
    #        res_mas.append(tmp)
    #res_mas.sort()
    #''.join(res_mas)
    #print(res_mas)
    mass = []
    mass.append("")
    for i in range(1, len(text)):
        mass = prohod(mass, text, i)
    mass.append(text)
    for chars in mass:
        if chars == '':
            res_mas.append(0)
        else:
            tmp = 0
            i = 0
            while i < len(chars):
                tmp += Mass_table[chars[i]]
                i += 1
            res_mas.append(tmp)
    res_mas.sort()
    print(' '.join([str(i) for i in res_mas]))