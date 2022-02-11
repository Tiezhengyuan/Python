# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:07:07 2015

@author: yuan
"""
#character replacement in a string
DNA='ATTCGTATCTTTATATATGGGG'
print 'IN:', DNA

#method 1
print '\nreplace all:', DNA.replace('AT', 'ta')
print 'replace the first two:', DNA.replace('AT', 'ta', 2)
print 'replace the last two:', DNA[::-1].replace('AT', 'ta', 2)[::-1]

#method 2
import re
print '\nreplace all:', re.sub('AT', 'ta', DNA)
print 'replace the first two:', re.sub('AT', 'ta', DNA, 2)
print 'replace the last two:', re.sub('AT', 'ta', DNA[::-1],2)[::-1]

#method 3: return the number of replacements
import re
print '\ntuple output:', re.subn('AT', 'ta', DNA)



