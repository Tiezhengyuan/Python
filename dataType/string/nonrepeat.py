# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:23:39 2017

@author: yuan
"""

#Given a string, find the length of the longest substring without repeating characters.

class string:
    def __init__(self, string):
        self.str=string
        self.str_len=len(self.str)
        #print self.str
        
    def seed_loop(self):
        #initiate
        pool_str=list(self.str)
        pool_index=range(self.str_len)
        #print pool_index
        n=0
        longest=1
        out_str=self.str[0]
        while (len(pool_str)>0):
            test_str=pool_str.pop()
            last_index=pool_index.pop()
            #print pool_str
            next_index=last_index+1
            if next_index<self.str_len:
                next_chr=self.str[next_index]
                if next_chr not in test_str:
                    test_str+=next_chr
                    pool_str.append(test_str)
                    pool_index.append(next_index)
                    if longest==len(test_str):
                        out_str.append(test_str)
                    elif longest<len(test_str):
                        out_str=[test_str]
                        longest=len(test_str)
        print 'longest nonrepeated substring:', out_str
        return out_str
        
if __name__=='__main__':
    
    #s="abcabcbb"
    #s="bbbbbbbbbb"
    #s="pwwkew"
    s='qewiprfavskdvnxc.,fghwerdtuiwrtyhreoiq;wfnvgjbx.dk,mcwerotg[yeafrvcdsvfbnm,yjyertw'
    string(s).seed_loop()

    print 'ok'