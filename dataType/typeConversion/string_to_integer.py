# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:08:09 2015

@author: yuan
"""

#convert a string to numeric type
import re

class convert_string:
    def __init__(self, string):
        self.minus=0
        #remove plus or minus
        string=re.sub('^\+*|\s', '', string)
        if re.search('^\-', string):
            string=re.sub('^-*', '', string)
            self.minus=1
        if re.search('\.', string):
            self.str1, self.str2=string.split('.')
        else:
            self.str1=string
            self.str2=''
        
    def str_to_int(self):
        str_int=0
        #integer part
        for c in self.str1:
            if re.search('[0-9]', c):
                str_int = str_int*10 + int(c)
            else:
                break
        #decimal part
        if not self.str2=='':
            n=float(10)
            for i in self.str2:
                if re.search('[0-9]', i):
                    str_int += int(i)/n
                    n *= 10
                    #print i,int(i)/n
                else:
                    break    
        if self.minus==1:
            str_int=-str_int
        return str_int

if __name__ == "__main__":
    strs=['123','-123','+123', '123fgds435', '  123  ', 'abc','-123ads', '++123', 
      '--123', '0', '123.56', '123.335gf4','3244444444444444444444444444444444']

    for str in strs:
        s=convert_string(str)        
        str_int=s.str_to_int()
        print (str, '\t<', str_int, '>')