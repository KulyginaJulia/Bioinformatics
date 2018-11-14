# Script to easily count pattern in genome

import sys
Codon_table = {'AAA' : 'K',
               'AAC' : 'N',
               'AAG' : 'K',
               'AAU' : 'N',
               'ACA' : 'T',
               'ACC' : 'T',
               'ACG' : 'T',
               'ACU' : 'T',
               'AGA' : 'R',
               'AGC' : 'S',
               'AGG' : 'R',
               'AGU' : 'S',
               'AUA' : 'I',
               'AUC' : 'I',
               'AUG' : 'M',
               'AUU' : 'I',
               'CAA' : 'Q',
               'CAC' : 'H',
               'CAG' : 'Q',
               'CAU' : 'H',
               'CCA' : 'P',
               'CCC' : 'P',
               'CCG' : 'P',
               'CCU' : 'P',
               'CGA' : 'R',
               'CGC' : 'R',
               'CGG' : 'R',
               'CGU' : 'R',
               'CUA' : 'L',
               'CUC' : 'L',
               'CUG' : 'L',
               'CUU' : 'L',
               'GAA' : 'E',
               'GAC' : 'D',
               'GAG' : 'E',
               'GAU' : 'D',
               'GCA' : 'A',
               'GCC' : 'A',
               'GCG' : 'A',
               'GCU' : 'A',
               'GGA' : 'G',
               'GGC' : 'G',
               'GGG' : 'G',
               'GGU' : 'G',
               'GUA' : 'V',
               'GUC' : 'V',
               'GUG' : 'V',
               'GUU' : 'V',
               'UAA' : '',
               'UAC' : 'Y',
               'UAG' : '',
               'UAU' : 'Y',
               'UCA' : 'S',
               'UCC' : 'S',
               'UCG' : 'S',
               'UCU' : 'S',
               'UGA' : '',
               'UGC' : 'C',
               'UGG' : 'W',
               'UGU' : 'C',
               'UUA' : 'L',
               'UUC' : 'F',
               'UUG' : 'L',
               'UUU' : 'F'
               }
def reverse(str):
    newstr = ""
    for char in str:
        if char == "A":
            newstr += "T"
            continue
        if char == "T":
            newstr += "A"
            continue
        if char == "G":
            newstr += "C"
            continue
        if char == "C":
            newstr += "G"
            continue
    tmp_res = newstr[::-1]
    return tmp_res

def out_codon(str):
    peptide = ''
    for i in range(0, len(str)-2, 3):
        peptide += Codon_table.get(str[i:i+3])
    return peptide
        
def transkrib(str):
    newstr = ""
    for char in str:
        if char == "T":
            newstr += "U"
        else:
            newstr += char
    return newstr

# main program
if __name__ == "__main__":
    text = str(sys.stdin.readlines(1))
    text = text[2:len(text) - 4]
    peptide = str(sys.stdin.readlines(1))
    peptide = peptide[2:len(peptide) - 4]
    frequency = {}
    inv_frequency = {}

    res = []
    while i < len(text) - len(peptide) * 3 + 1:
        string = text[i:i + len(peptide) * 3]
        if out_codon(transkrib(string)) == peptide:
            res.append(string)
        i += 1
    text = reverse(text)

    while i < len(text) - len(peptide) * 3 + 1:
        string = text[i:i + len(peptide) * 3]
        if out_codon(transkrib(string)) == peptide:
            res.append(reverse(string))
        i += 1
    print(res)
    words = ' '.join([str(i) for i in res])
    print(words)