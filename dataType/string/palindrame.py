# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:23:39 2017

@author: yuan
"""

#Given a string, find the length of the longest palindromic substring
import itertools
import re

class string:
    def __init__(self, string):
        self.str=string
        self.str_len=len(self.str)
        self.pool_index=[]

        self.out=[]
        self.longest=0
        #print self.str
        
    def rev_com(self,dna_seq):
        #reverse
        rev_seq=dna_seq[::-1]
        #print rev_seq
        #compliment
        rdict={'A':'T','T':'A','G':'C','C':'G'}
        robj = re.compile('|'.join(rdict.keys()))
        rev_com = robj.sub(lambda m: rdict[m.group(0)], rev_seq)
        #print rev_com
        return rev_com
###        
    def search_loop(self, func):
        #print self.pool_index
        while (len(self.pool_index)>0):
            start_index,end_index=self.pool_index.pop()
            next_left, next_right=start_index-1, end_index+1
            #judge palindrome
            tag=0
            if next_left>=0 and next_right<self.str_len:
                new_str=self.str[next_left:next_right]
                palindromic_str=func(new_str)
                #print new_str, reverse_str
                if new_str==palindromic_str:
                    self.pool_index.insert(0,(next_left,next_right))
                    tag=1
            #update
            if tag==0:
                current_len=end_index-start_index
                current=(self.str[start_index:end_index], start_index+1, end_index)
                #print self.str[start_index:end_index]
                if self.longest==current_len:
                    self.out.append(current)
                elif self.longest<current_len:
                    self.out=[current]
                    self.longest=current_len
#
    def longest_dna(self):
        #initiate index
        #at least 2 characters for a palindromic string
        for x,y in itertools.izip(xrange(0, self.str_len-2), xrange(2,self.str_len)):
            rc_seq=self.rev_com(self.str[x:y])
            if self.str[x:y]==rc_seq: 
                self.pool_index.append((x,y))
                #print self.str[x:y], rc_seq, x,y
        #find longest palindromic sequence
        self.search_loop(self.rev_com)
        print 'longest palindromic DNA-seq:', self.out
        return self.out

    def longest_words(self):
        #initiate index
        #at least 2 characters for a palindromic string
        for x,y in itertools.izip(xrange(0, self.str_len-2), xrange(2,self.str_len)):
            if self.str[x:y]==self.str[x:y][::-1]: 
                self.pool_index.append((x,y))
        #at least 3 characters for a palindromic string
        for x,y in itertools.izip(xrange(0, self.str_len-3), xrange(3,self.str_len)):
            if self.str[x:y]==self.str[x:y][::-1]: 
                self.pool_index.append((x,y))
        #find longest palindromic words
        self.search_loop(lambda x: x[::-1])
        print 'longest palindromic substring:', self.out      
        return self.out
        
if __name__=='__main__':
    
    #s="babad"
    #s="cbbd"
    s='3344563533452435017542224422289057489017345674378283476'
    string(s).longest_words()
    
    s="GAATTCAATGCCATGATGATGATTAGAATTCTTACGACACAACAACACCGCGCTTGACGGCGGCGGATGGATGCCGCGATCAGACGTTCAACGCCCACGTAACGTAACGCAACGTAACCTAACGACACTGTTAACGGTACGAT"
    #print string(s).rev_com('GAATTC')
    #string(s).longest_dna()

    print 'ok'