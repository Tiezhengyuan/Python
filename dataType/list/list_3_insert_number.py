# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:42:02 2015

@author: yuan
"""
#insert a number into a list
class insert_element:
    
    def __init__(self, arr):
        self.arr=arr
        self.len=len(arr)
        self.index=0
        print ('Old list:', arr)
    
    def insert(self, number):
        if number<self.arr[0]:
            self.arr.insert(0,number)
            self.index=0
        elif number > self.arr[-1]:
            self.arr.append(number)
            self.index=self.len
        else:
            middle_index=int(self.len/2)
            middle=self.arr[middle_index]
            print ('middle element=',middle)
            if number<middle:
                index_range=range(0,middle_index)
            elif number >middle:
                index_range=range(middle_index, self.len)
            else:
                index_range=[middle_index]
            index_range.reverse()
        
            #insert
            find=0
            for i in index_range:
                if number>= self.arr[i]:
                    self.arr.insert(i+1,number)
                    self.index=i+1
                    find=1
                    break
        print ('New list:',self.arr)
        print ('The index of the inserted number:', self.index)
        return self.arr, self.index


#main programming
arr=[2,35,53,35,4,8,54,43,98,12,33]
arr.sort()
insert=insert_element(arr)
#
insert.insert(1)   
insert.insert(35)   
insert.insert(100)   

