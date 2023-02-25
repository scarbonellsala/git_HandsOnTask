# -*- coding: utf-8 -*-
"""
Python script to compute the percentage of each nucleotide
of a given DNA sequence

"""
import sys
import re


def validate_dna(seq):
    if not re.search('^[ACGT]+$', seq):
        print('ERROR, input needs to be DNA sequence', file=sys.stderr)
        exit(1)


def main():
    seq = input("Type a sequence: ")
    seq = seq.upper()
    validate_dna(seq)
    total_bases = len(seq)
    for base in 'ACTG':
        percentage = ((seq.count(base) / total_bases) * 100)
        print('The percentage of {0} is {1}'.format(base,
                                                    round(percentage, 3)))


main()
