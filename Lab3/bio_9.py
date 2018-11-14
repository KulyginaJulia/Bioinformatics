# Script to easily count pattern in genome

import sys
Table_mass = ['57', '71', '87', '97', '99', '101', '103', '113', '114', '115', '128', '129', '131', '137', '147',
              '156', '163', '186']
def prohod(mass, text, num):
    i = 0
    while i < len(text):
        if (i + num > len(text)):
            if num == len(text):
                break;
            free = len(text) - i
            second = num - free
            tmp = 0
            count = i
            while count < len(text):
                tmp += int(text[count])
                count += 1
            count = 0
            while count < second:
                tmp += int(text[count])
                count += 1
            mass.append(tmp)
        else:
            tmp = 0
            count = num
            count_text = i
            while count > 0:
                tmp += int(text[count_text])
                count -= 1
                count_text += 1
            mass.append(tmp)
        i += 1
    return mass

def CycloSpectrum(text):
    mass = []
    text = text[2:len(text)]
    text_list = text.split(' ')
    for i in range(1, len(text_list) + 1):
        mass = prohod(mass, text_list, i)

    mass.append(0)
    mass.sort()
    stringa = ' '.join([str(i) for i in mass])
    return stringa

def LinearSpectrum(peptide):
    res = []
    i = 0
    k = 1
    peptide_list = peptide.split(' ')
    peptide_list.remove('0')
    while k < len(peptide_list):
        while (i+k <= len(peptide_list)):
            j = 0
            tmp = 0
            while j < k:
                tmp += int(peptide_list[i + j])
                j += 1
            res.append(str(tmp))
            i += 1
        i = 0
        k += 1

    if len(peptide_list) != 0:
        tmp = 0
        for pep in peptide_list:
            tmp += int(pep)
        res.append(str(tmp))
        res.append('0')
    res.sort()
    return res

def Mass(peptide):
    mass = 0
    pep_list = peptide.split(' ')
    for pep in pep_list:
        mass += int(pep)
    return mass

def ParentMass(Spectrum_list):
    return int(Spectrum_list[-1])

def Expand(Peptides):
    res_Peptides = []
    j = 0
    while j < len(Peptides):  # for peptide in Peptides:
        pep = Peptides[j]
        for mas in Table_mass:
            res_Peptides.append(pep + ' ' + mas)
        Peptides.remove(pep)
    return res_Peptides

def consist(Spectrum, peptide):
    for p in LinearSpectrum(peptide):
        if p not in Spectrum:
            return False
    return True

def main_prog(Spectrum):
    Peptides = ['0']
    output = []
    i = 0
    Spectrum_list = Spectrum.split(' ')
    parent_mass = ParentMass(Spectrum_list)
    while len(Peptides) != 0:
        Peptides = Expand(Peptides)
        i = 0
        while i < len(Peptides):
            peptide = Peptides[i]
            mass_pep = Mass(peptide)
            if (mass_pep == parent_mass):
                stringa_cycloSpectrum = CycloSpectrum(peptide)
                if stringa_cycloSpectrum == Spectrum:
                    output.append(peptide)
                Peptides.remove(peptide)
            else:
                if not consist(Spectrum, peptide):
                    Peptides.remove(peptide)
                else:
                    i += 1
    output_res = []
    for peptide in output:
        peptide = str(peptide[2:len(peptide)])
        peptide = peptide.replace(' ', '-')
        output_res.append(peptide)
    return output_res

# main program
if __name__ == "__main__":
    #Spectrum = str(sys.stdin.readlines(1))
    #Spectrum = Spectrum[2:len(Spectrum) - 4]
    Spectrum = '0 113 113 113 113 113 114 114 114 114 114 128 128 128 128 128 129 129 129 129 129 227 227 227 227 227 242 242 242 242 242 242 242 242 242 242 257 257 257 257 257 355 355 355 355 355 356 356 356 356 356 370 370 370 370 370 371 371 371 371 371 484 484 484 484 484 484 484 484 484 484 484 484 484 484 484 484 484 484 484 484 597 597 597 597 597 598 598 598 598 598 612 612 612 612 612 613 613 613 613 613 711 711 711 711 711 726 726 726 726 726 726 726 726 726 726 741 741 741 741 741 839 839 839 839 839 840 840 840 840 840 854 854 854 854 854 855 855 855 855 855 968 968 968 968 968 968 968 968 968 968 968 968 968 968 968 968 968 968 968 968 1081 1081 1081 1081 1081 1082 1082 1082 1082 1082 1096 1096 1096 1096 1096 1097 1097 1097 1097 1097 1195 1195 1195 1195 1195 1210 1210 1210 1210 1210 1210 1210 1210 1210 1210 1225 1225 1225 1225 1225 1323 1323 1323 1323 1323 1324 1324 1324 1324 1324 1338 1338 1338 1338 1338 1339 1339 1339 1339 1339 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1452 1565 1565 1565 1565 1565 1566 1566 1566 1566 1566 1580 1580 1580 1580 1580 1581 1581 1581 1581 1581 1679 1679 1679 1679 1679 1694 1694 1694 1694 1694 1694 1694 1694 1694 1694 1709 1709 1709 1709 1709 1807 1807 1807 1807 1807 1808 1808 1808 1808 1808 1822 1822 1822 1822 1822 1823 1823 1823 1823 1823 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 1936 2049 2049 2049 2049 2049 2050 2050 2050 2050 2050 2064 2064 2064 2064 2064 2065 2065 2065 2065 2065 2163 2163 2163 2163 2163 2178 2178 2178 2178 2178 2178 2178 2178 2178 2178 2193 2193 2193 2193 2193 2291 2291 2291 2291 2291 2292 2292 2292 2292 2292 2306 2306 2306 2306 2306 2307 2307 2307 2307 2307 2420'
    output_res = main_prog(Spectrum)
    print(' '.join([i for i in output_res]))


