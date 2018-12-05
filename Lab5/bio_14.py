# Script to find motifs
def ProfileString_to_Matrix(Profile, k):
    n = 4
    a = [[0] * k for i in range(n)]
    Profile_split = Profile.split('\n')

    for i in range(n):
        Profile_elems = Profile_split[i].split(' ')
        for j in range(k):
            a[i][j] = Profile_elems[j]
    return a

def ProbabilityString_Profile(String, Profile, k):
    Pr = 1.0
    for char, number in zip(String, range(k)):
        if char == 'A':
            Pr *= float(Profile[0][number])
            continue
        if char == 'C':
            Pr *= float(Profile[1][number])
            continue
        if char == 'G':
            Pr *= float(Profile[2][number])
            continue
        if char == 'T':
            Pr *= float(Profile[3][number])
            continue
    return Pr

def ProfileMostProbability(DNA, k, Profile):
    i = 0
    dict = {}
    while (i < len(DNA) - k + 1):
        window = DNA[i : i + k]
        probability = ProbabilityString_Profile(window, Profile, k)
        dict[probability] = window
        i += 1

    max_prob = max(dict.keys())
    return dict[max_prob]

# main program
if __name__ == "__main__":

   # stringText = "CCCCTATAGTTCTTGGTGCAGCGTGCACCCTCGTCTGGTTCGGATACGGGCCTGCCAGGA"
    stringText = input()

    k = 5
    k = int(input())
#    Profile = '''0.583 0.25 0.417 0.25 0.167
#0.083 0.25 0.417 0.333 0.25
#0 0.25 0.167 0 0.333
#0.333 0.25 0 0.417 0.25'''
    Profile = ""
    for i in range(4):
        Profile += input()
        Profile += '\n'

    Profile = ProfileString_to_Matrix(Profile, k)
    output = ProfileMostProbability(stringText, int(k), Profile)
    print(output)
    if output == 'ATACG':
        print('True')
    else:
        print('False')
