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
def Theoretical_spectrum(peptide):
    res_mas = []
    mass = []
    mass.append("")
    for i in range(1, len(peptide)):
        mass = prohod(mass, peptide, i)
    mass.append(peptide)
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
    return res_mas

def main_prog(peptide, Spectrum):
    theoret = Theoretical_spectrum(peptide)
    Spectrum = Spectrum.split(' ')
    count = 0
    score = 0
    i = 0
    j = 0
    while (i < len(theoret) and j < len(Spectrum)):
        if (theoret[i] == int(Spectrum[j])):
            i += 1
            j += 1
            score += 1
        else:
            if (theoret[i] < int(Spectrum[j])):
                i += 1
            else:
                j += 1
    return score

    for mass_th in theoret:
        for mass_exp in Spectrum:
            if int(mass_exp) == mass_th:
                count += 1
    return count


# main program
if __name__ == "__main__":
    #peptide = str(sys.stdin.readlines(1))
    #peptide = peptide[2:len(peptide) - 4]
    #Spectrum = str(sys.stdin.readlines(1))
    #Spectrum = Spectrum[2:len(Spectrum) - 4]

    peptide = 'NQQL'
    Spectrum = '0 99 113 114 128 227 257 299 355 356 370 371 484'
    Score = main_prog(peptide, Spectrum)
    print(Score)

