# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:41:41 2015

@author: yuan
"""

import sys
import re

#memory usage of a string measured by bit
print ('A blank string', sys.getsizeof(''))
print ('A string with 10 characters', sys.getsizeof('abcdefghij'))
print ('A string with 10 characters', sys.getsizeof('1234567890'))

#integer would require less memory than sting
print ('A integer with 1 characters', sys.getsizeof(int('1') ))
print ('A integer with 10 characters', sys.getsizeof(int('1234567890') ))
print ('A float number with 10 characters', sys.getsizeof(float('1234567890') ))
print ('A integer with more than 10 characters', sys.getsizeof(int('1234567890')*10 ))


#
DNA_seed='CGAACGGAACAGTGGAATTCTCGGGTGCCCAGGAACTCCAGTCACCCGTCCATCTCGTATGCCGTCTTCTGCTTGAAAAAAAAAAAAACACGACAGACATA'
for i in range(1,3):
    DNA=(10**i)*DNA_seed
    len_dna=len(DNA)
    print ('A %s nt DNA sequence use memory %s byte'% (len_dna, sys.getsizeof(DNA)))

    #convert DNA string into numeric DNA to save memory
    #A=1, T=3,G=2, C=4, N=0
    int_dna=DNA.upper()
    #int_dna=re.sub('A', '1', int_dna)
    #int_dna=re.sub('T', '3', int_dna)
    #int_dna=re.sub('G', '2', int_dna)
    #int_dna=re.sub('C', '4', int_dna)
    #int_dna=re.sub('N', '5', int_dna)
    adict={'A':'1', 'T':'3', 'G':'2', 'C':'4', 'N':'5'}
    rx=re.compile('|'.join(map(re.escape, adict)))
    int_dna=rx.sub(lambda x: adict[x.group(0)], int_dna)
    int_dna=int(int_dna)
    #print int_dna
    print ('The numeric DNA sequence require bit:', sys.getsizeof(int_dna))


