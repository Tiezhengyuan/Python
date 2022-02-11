from typing import List

class RecursionList:
    def sum_list(self, mylist):
        """
        #sum of all numbers of a list
        #sum(1)=list[0], sum(2)=list[1]+sum(1), 
        # sum(n)=list[n-1]+sum(n-1)
        """
        if not isinstance(mylist, list) or mylist == []:
            return None
        if len(mylist)==1:
            return mylist[0]
        else:
            return mylist[0] + self.sum_list(mylist[1:])

    def capitalize_list(self, mylist):
        """
        #capitalize all letters of worlds in a list
        #func(0)=[], func(1)=[list[0].upper()], 
        # func(2)=func(1)+[list[1].upper()], , 
        # func(n)=func(n-1)+[list[n-1].upper()]
        """
        if mylist == []:
            return []
        else:
            el = mylist[0].upper()
            return [el] + self.capitalize_list(mylist[1:])


    def flatten_list(self, mylist):
        """
        #flatten nested list
        #func(0)=[], func(1)=list[0] or 
        # [list[0]], func(2) = (list[1] or [list[1]])+func(1)
        #func(n) = (list[n-1] or [list[n-1]])+func(n-1)
        #if multiple embeded list: 
        # func(n) = func(list[n-1])+func(n-1)
        """
        if mylist==[]:
            return []
        else:
            if isinstance(mylist[0], list):
                return self.flatten_list(mylist[0]) + self.flatten_list(mylist[1:])
            return [mylist[0]] + self.flatten_list(mylist[1:])
    
    def swap(self, mylist, a, b):
        if a<b and 0 <= a < len(mylist) and 0 <= b < len(mylist):
            mylist[a], mylist[b] = mylist[b], mylist[a]
        if a<b:
            self.swap(mylist, a+1, b-1)
        
    def reverse_list(self, mylist):
        """
        reverse in-place
        """
        if len(mylist) > 1:
            start = 0
            end = len(mylist) -1
            self.swap(mylist, start, end)
        return mylist
    
    def count_list(self, mylist):
        if len(mylist)==0:
            return 0
        else:
            el = mylist[0]
            return len(el) + self.count_list(mylist[1:])


    def recur_list(self, c, L, R):
        if L < R:
            if c[L]> c[R]:
                c[L], c[R] = c[R], c[L]
            self.recur_list(c, L+1, R)
        
    def sort_ascending(self, c):
        if len(c) == 0:
            return []
        for P in range(len(c)-1, -1, -1):
            self.recur_list(c, 0, P)


    def insert_sorted(self, mylist, value):
        """
        #insert a number into a sorted list using recursion
        """
        if mylist == []:
            return [value]
        elif value <= mylist[0]:
            mylist.insert(0, value)
            return mylist
        elif value >= mylist[-1]:
            mylist.append(value)
            return mylist
        else:
            return [mylist[0]] + self.insert_sorted(mylist[1:], value)


    def search_value(self, s: List, target):
        """
        binary search sorted list: return index or -1
        """
        if len(s) == 0:
            return -1
        L, R = 0, len(s) - 1
        return self.binary_search(s, L, R, target)

    def binary_search(self, s, L, R, target):
        if L > R:
            return -1
        M = int((L+R)/2)
        if s[M] == target:
            if M == 0 or (M > 0 and s[M-1] != target):
                return M
        elif s[M] < target:
            return self.binary_search(s, M+1, R, target)
        return self.binary_search(s, L, M-1, target)
    