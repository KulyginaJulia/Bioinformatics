# Script to easily count pattern in genome

import sys

# main program
if __name__ == "__main__":
    length_cycle_peptide = str(sys.stdin.readlines(1))
    length_cycle_peptide = length_cycle_peptide[2:len(length_cycle_peptide) - 4]
    length_cycle_peptide = int(length_cycle_peptide);
    number_subpeptide = length_cycle_peptide * (length_cycle_peptide - 1)

    print(number_subpeptide)