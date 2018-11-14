# Script to easily count pattern in genome

import sys
Table_mass = ['57', '71', '87', '97', '99', '101', '103', '113', '114', '115', '128', '129', '131', '137', '147',
              '156', '163', '186']

def LinearSpectrum(peptide):
    res = []
    i = 0
    k = 1
    peptide_list = peptide.split(' ')
    peptide_list.remove('0')
    while k < len(peptide_list):
        while (i + k - 1 < len(peptide_list)):
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

def Expand(Peptides):
    res_Peptides = []
    j = 0
    while j < len(Peptides):
        pep = Peptides[j]
        for mas in Table_mass:
            res_Peptides.append(pep + ' ' + mas)
        Peptides.remove(pep)
    return res_Peptides

def Mass(peptide):
    mass = 0
    pep_list = peptide.split(' ')
    for pep in pep_list:
        mass += int(pep)
    return mass
def ParentMass(Spectrum_list):
    return int(Spectrum_list[-1])

def Score(peptide, Spectrum):
    theoret = LinearSpectrum(peptide)
    Spectrum = Spectrum.split(' ')
    count = 0
    i = 0
    j = 0
    while (i < len(theoret) and j < len(Spectrum)):
        if (int(theoret[i]) == int(Spectrum[j])):
            i += 1
            j += 1
            count += 1
        else:
            if (int(theoret[i]) < int(Spectrum[j])):
                i += 1
            else:
                j += 1
    return count

def sortByMaxScore(inputStr):
        return inputStr[1]
def Trim(Leaderboard, Spectrum, N):
    res = []
    score_list = []
    for i in Leaderboard:
        tmp = Score(i, Spectrum)
        score_list.append([i, tmp])

    score_list.sort(key=sortByMaxScore)
    score_list.reverse()
    min_length = min(len(score_list), N)
    flag = True
    j = 0
    while (flag):
        if j < min_length:
            res.append(score_list[j][0])
            j += 1
        else:
            if((j < len(score_list)) and (score_list[min_length-1][1] == score_list[j][1])):
                res.append(score_list[j][0])
                j += 1
            else:
                flag = False

    return res

def main_prog(N, Spectrum):
    Leaderboard = ['0']
    Spectrum_list = Spectrum.split(' ')
    parent_mass = ParentMass(Spectrum_list)
    LeaderPeptide = '0'
    while len(Leaderboard) != 0:
        Leaderboard = Expand(Leaderboard)
        i = 0
        while i < len(Leaderboard):
            peptide = Leaderboard[i]
            mass_pep = Mass(peptide)
            if (mass_pep == parent_mass):
                if (Score(peptide, Spectrum) > Score(LeaderPeptide, Spectrum)):
                    LeaderPeptide = peptide
                i += 1
            else:
                if (mass_pep > parent_mass):
                    Leaderboard.remove(peptide)
                else:
                    i += 1
        Leaderboard = Trim(Leaderboard, Spectrum, N)

    LeaderPeptide_list = LeaderPeptide.split(' ')
    LeaderPeptide_list.remove('0')
    LeaderPeptide = '-'.join(LeaderPeptide_list)
    return LeaderPeptide



# main program
if __name__ == "__main__":
   # N_text = str(sys.stdin.readlines(1))
   # N_text = N_text[2:len(N_text) - 4]
   # N = int(N_text)
    #Spectrum = str(sys.stdin.readlines(1))
   # Spectrum = Spectrum[2:len(Spectrum) - 4]

    N = 9
    Spectrum = '0 114 114 114 228 228 228 242 242 342' #'0 71 101 103 113 114 128 131 156 156 172 199 232 242 259 269 270 287 300 303 313 372 372 373 388 398 400 414 431 459 469 486 501 501 503 528 545 570 572 572 587 604 614 642 659 673 675 685 700 701 701 760 770 773 786 803 804 814 831 841 857 874 901 917 917 942 945 959 960 970 972 1002 1073'

    output = main_prog(N, Spectrum)
    print(output)

