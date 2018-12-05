# Script to find motifs
def CreateProfile(Motifs):
    n = 4
    m = len(Motifs[0])
    Profile = [[0] * m for i in range(n)]

    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            char = Motifs[i][j]
            if char == 'A':
                Profile[0][j] += 1
            if char == 'C':
                Profile[1][j] += 1
            if char == 'G':
                Profile[2][j] += 1
            if char == 'T':
                Profile[3][j] += 1

    for i in range(n):
        for j in range(m):
            Profile[i][j] += 1
    for i in range(n):
        for j in range(m):
            Profile[i][j] = Profile[i][j] / len(Motifs)

    return Profile

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
    best_probability = 0.0
    dict[best_probability] = DNA[0 : 0 + k]
    while (i < len(DNA) - k + 1):
        window = DNA[i : i + k]
        probability = ProbabilityString_Profile(window, Profile, k)
        if (probability > best_probability):
            best_probability = probability
            dict[best_probability] = window
        i += 1

    return dict[best_probability]

def Score(Motifs):
    Score = 0
    for j in range(len(Motifs[0])):
        f = 0
        dict_count = [0, 0, 0, 0]
        for i in range(len(Motifs)):
            if Motifs[i][j] == 'A':
                dict_count[0] += 1
                f += 1
                continue
            if Motifs[i][j] == 'C':
                dict_count[1] += 1
                f += 1
                continue
            if Motifs[i][j] == 'G':
                dict_count[2] += 1
                f += 1
                continue
            if Motifs[i][j] == 'T':
                dict_count[3] += 1
                f += 1
                continue
        Score += f - max(dict_count)
    return Score

def GreedyMotifSearch(DNA, k, t):
    BestMotifs = []
    for i in range(t):
        BestMotifs.append(DNA[i][0 : k])

    for i in range(len(DNA[0]) - k + 1):
        Motifs = []
        Motifs.append(DNA[0][i:i + k])

        for j in range(1, t):
            Profile = CreateProfile(Motifs)
            Motifs.append(ProfileMostProbability(DNA[j], k, Profile))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs.copy()

    return BestMotifs

# main program
if __name__ == "__main__":
    k = 5
    t = 8
    DNA = '''AGGCGGCACATCATTATCGATAACGATTCGCCGCATTGCC
ATCCGTCATCGAATAACTGACACCTGCTCTGGCACCGCTC
AAGCGTCGGCGGTATAGCCAGATAGTGCCAATAATTTCCT
AGTCGGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG
AACCGGACGGCAACTACGGTTACAACGCAGCAAGAATATT
AGGCGTCTGTTGTTGCTAACACCGTTAAGCGACGGCAACT
AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG
AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA'''
    DNA = DNA.split('\n')
    output = GreedyMotifSearch(DNA, k, t)
    print('\n'.join(output))

