# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:48:17 2015

@author: yuan
"""

#methods of loops of a list

l=[1,2,3,4,9,10]
print ('The given list:', l)

####################3
##method 1:
for element in l:
    print(element)

#method 2:
for index in range(len(l)):
    element=l[index]
    print(index, element)

#print "method 3:"
for index, element in enumerate(l):
    print(index, element)
    
#reversed loops
print ('reversed loops of method 1:')
for element in l[::-1]:
    print (element)
    
print ('reversed loops of method 2:')
r_index=range(len(l))
r_index.reverse()
for index in r_index:
    element=l[index]
    print (index, element)

print ("reversed loops of method 3:")
for index, element in enumerate(l[::-1]):
    print (index, element)

#partial loop
print ("loops of the first 3 elements:")
for element in l[:3:1]:
    print (element)

#print "loops of the last 3 elements:"
for element in l[-3::1]:
    print (element)

#print "reversed loops of the last 3 elements:"
for element in l[:-4:-1]:
    print (element)
    
#print "loops of elements with index from 2 to 5:"
for element in l[2:6]:
    print (element)
 
#print "loops of elements with odd index:"
for element in l[1::2]:
    print (element)

#print "loops of elements with even index:"
for element in l[2::2]:
    print (element)
    
print('looping through multiple lists at a time:')
a=range(10)
b=range(40,50)
c=range(80,900)
#different length is allowed.
for x,y,z in zip(a,b,c):
    print (x,y,z)


