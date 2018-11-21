# Script to find motifs
import math
import sys
def Differense(str1, str2):
    diffs = 0
    for char1, char2 in zip(str1, str2):
        if (char1 != char2):
            diffs += 1
    return diffs

def K_mers(k):
    member_in_dnk = ["A", "C", "G", "T"]
    result = set()
    base = len(member_in_dnk)
    for i in range(base ** k):
        pattern_ = ''
        while(len(pattern_) != k):
            tmp = (i % base)
            pattern_ += member_in_dnk[tmp]
            i = math.floor(i / base)

        result.add(pattern_)
    return result

def Min_Hamming_distance(Pattern, DNA, k):
    distance = 0
    for string_dna in DNA:
        min_dist = float('inf')
        for i in range(len(string_dna) - k + 1):
            d = Differense(Pattern, string_dna[i:i + k])
            if d < min_dist:
                min_dist = d

        distance += min_dist
    return distance

def MedianString(DNA, k):
    Patterns = []
    distance = float('inf')
    Motifs = K_mers(k)
    median = ''
    i = 0
    for motif in Motifs:
        d = Min_Hamming_distance(motif, DNA, k)
        if distance > d:
            distance = d
            median = motif
    return median

    return median

# main program
if __name__ == "__main__":

    #k = int(input())
   # string_split = []
   # while True:
    #    temp = sys.stdin.readline()
     #   if temp != '':
   #         string_split.append(str(temp).replace('\n', ''))
    #    else:
     #       break
    #string_split = sys.stdin.read()
    k = 5
   # d = 1
    string_split = ['GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA', 'TATATCCACATGACCTCGACAACGCACGGTCGAAT', 'TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC',
                    'TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT', 'TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT', 'AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT',
                    'CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC', 'ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT', 'GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA',
                    'ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG']
#    string_split = collect_string.split('\n')

    output = MedianString(string_split, int(k))
    print(output)
    if output == 'ACTGT':
        print('True')
    else:
        print('False')
