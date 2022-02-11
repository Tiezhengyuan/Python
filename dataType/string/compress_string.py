# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:45:25 2015

@author: yuan
"""


import sys
import re
import zlib

def str_to_num(string):
    string=re.sub('A', '1', string)
    string=re.sub('T', '3', string)
    string=re.sub('G', '2', string)
    string=re.sub('C', '4', string)
    #string=re.sub('^N*|N*$', '', string)
    string=int(re.sub('N', '0', string))
    print string
    return string

    
#main program
if __name__=="__main__":


    seq='NNNNAACCCGTAGATCNCGATCTTGTTGGAATTCTCGGNGTGCCAAGGAACTCCAGTCACCCGTCCATCTCGTATGCCGTCTTCTGCTTGAAAAAAAAAAAAAAAACNNNN'
    print 'Memory usage (byte)'
    print 'string:', sys.getsizeof(seq)/8
    #
    num_seq=str_to_num(seq)
    print '\nnumeric string:', sys.getsizeof(num_seq)/8

    #
    zlib_seq=zlib.compress(seq)
    print '\nzlib string:', sys.getsizeof(zlib_seq)/8
    zlib_seq=zlib.compress(str(num_seq))
    print '\nzlib numeric string:', sys.getsizeof(zlib_seq)/8