# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:20:07 2015

@author: yuan
"""
#get a region with a given number
class search_region:
    def __init__(self, arr):
        self.arr=arr
        self.len=len(arr)
        self.index=0
        print 'Old list:', arr
    
    
        
    def get_region(self, number):
        if number<self.arr[0] or number>self.arr[-1]:
            print number, 'is out of this region!'
        else:
            middle_index=int(self.len/2)
            middle=self.arr[middle_index]
            print 'middle element=',middle
            if number<middle:
                a=0
                b=middle_index
            elif number >=middle:
                a=middle_index
                b=self.len
            while((b-a)>1):
                if self.arr[a+1]<=number:
                    a+=1
                if self.arr[b-1]>=number:
                    b-=1
            print self.arr[a], self.arr[b]
            return a,b

#main programming
arr=[2,35,53,4,8,54,43,98,12,33]
arr.sort()
#
sg=search_region(arr)
sg.get_region(97)
        