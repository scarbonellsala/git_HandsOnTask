# -*- coding: utf-8 -*-
"""
Python script to compute the percentage of each nucleotide of a given DNA sequence

"""

seq = input("Type a sequence: ")
total_bases = len (seq)
for base in 'acgt':
    percentage = ((seq.count(base) / total_bases)*100)
    print ('The percentage of {0} is {1}'.format(base, percentage))
    