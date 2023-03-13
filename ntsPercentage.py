# -*- coding: utf-8 -*-

"""

Python script to compute the percentage of each nucleotide
of a given DNA or RNA sequence

"""
import sys
import re

# Determine if the input fits better as DNA or RNA.

def DNA_or_RNA(seq):
    seq = seq.upper()
    if re.search('^[ACGTU]+$', seq):
        if re.search('T', seq) and re.search('U', seq):
    	    return "NOT"
        elif re.search('T', seq):
            return "DNA"
        elif re.search('U', seq):
            return "RNA"
    else:
        return "NOT"

# Compute % for the nucleotides of an input sequence.
def main():
    seq = input("Type a sequence: ")
    seq = seq.upper()
    seq_type = DNA_or_RNA(seq)
    total_bases = len(seq)
    if seq_type == "DNA":
        for base in 'ACTG':
            percentage = ((seq.count(base) / total_bases) * 100)
            print('The percentage of {0} is {1}'.format(base,
                                                    round(percentage, 3)))
    elif seq_type == "RNA":
        for base in 'ACUG':
            percentage = ((seq.count(base) / total_bases) * 100)
            print('The percentage of {0} is {1}'.format(base,
                                                    round(percentage, 3)))
    else:
        print("The sequence is probably not DNA nor RNA.")

main()

