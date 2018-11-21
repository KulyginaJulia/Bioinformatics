# Script to find motifs

import sys
def Differense(str1, str2):
    diffs = 0
    for char1, char2 in zip(str1, str2):
        if (char1 != char2):
            diffs += 1
    return diffs

def K_mers(Pattern):
    member_in_dnk = ["A", "C", "G", "T"]
    result = set()
    i = 0
    while i < len(Pattern):
        for j in member_in_dnk:
            result.add(Pattern[:i] + j + Pattern[i+1:])
        i += 1

    return result

def In_each_string(Pattern, String_DNA, d, k):
    for i in range(len(String_DNA) - k + 1):
        window = String_DNA[i:i + k]
        if (Differense(Pattern, window) <= d):
            return True
    return False

def MotifEnumeration(DNA, k, d):
    Patterns = []
    i = 0
    for string_in_DNA in DNA:
        for i in range(len(DNA[0])-k+1):
            pattern = string_in_DNA[i:i + k]
            Motifs = K_mers(pattern)
            for motif in Motifs:
                flag_meeting = True
                for j in range(len(DNA)):
                    if not In_each_string(motif, DNA[j], d, k):
                        flag_meeting = False
                        break
                if flag_meeting:
                    Patterns.append(motif)

    Patterns = set(Patterns)
    Patterns = list(sorted(Patterns))
    return ' '.join(Patterns)

# main program
if __name__ == "__main__":
    #k_text = input()
   # k = int(k_text)
    #d_text = input()
    #d = int(d_text)
    #collect_string = input()
    k, d = input().split()
    string_split = []
    while True:
        temp = sys.stdin.readline()
        if temp != '':
            string_split.append(str(temp).replace('\n', ''))
        else:
            break
    #string_split = sys.stdin.read()
   # k = 4
   # d = 1
    #collect_string = '''CACTGATCGACTTATC
#CTCCGACTTACCCCAC
#GTCTATCCCTGATGGC
#CAGGGTTGTCTTGTCT'''
#    string_split = collect_string.split('\n')

    output = MotifEnumeration(string_split, int(k), int(d))
    print(output)
    if output == 'CAGA CCTT CTCT CTTA CTTG CTTT GACT GATT GCCT GGCT GTCT TATC TCTG TCTT TGAC TTAT TTTC':
        print('True')
    else:
        print('False')
