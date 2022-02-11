# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:51:16 2015

@author: yuan
"""

#use of split(), rsplit(), partition()

print '\nsplit string by delimiter'
string='We,are,the,world'
print 'In:', string
print 'Out:', string.split(',')


print '\nsplit string by one or more white space'
string='We are  the world   '
print 'In:', string
print 'Out:', string.split()


print '\nsplit string by delimiter, Split from the right, rule the splited parts.'
string='We,are,the,world,and,great,day'
print 'In:', string
print 'Out:', string.rsplit(',')
print 'Out:', string.rsplit(',',1)
print 'Out:', string.rsplit(',',3)

print '\nsplit string by the first seperate and return tuple'
print 'In:', string
print 'Out:', string.partition(',')
print 'Out:', string.partition(' ')


print '\nsplit string into characters'
string='dsf3y43b4'
print 'In:', string
print 'Out:', list(string)


print '\nsplit a string into words by multiple seperates'

import re
string='One solution has been to add some: since Singapore has expanded by over one-fifth, from 58,000 hectares (224.5 square miles) to nearly 72,000, by filling in the sea with imported sand.'
print 'In:', string
a=re.split('[\s:()]', string)
print 'Out:', map( lambda x: re.sub("\.$|,", "", x), a)

