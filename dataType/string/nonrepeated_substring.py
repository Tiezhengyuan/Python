# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    def duplicated(self):
        dupl = []
        while len(self.str) > 0:
            i = self.str[0]
            self.str = self.str[1:]
            if i in self.str:
                if i not in dupl: 
                    dupl.append(i)
                self.str.replace(i,'')
        return dupl
    
    def nonrepeated(self, seedLen = None):
        if seedLen is None:
            max_len = len(self.str)
        else:
            max_len = seedLen
        max_str = []
        while max_len > 0:
            for i in range(0, len(self.str)-max_len+1):
                sub_str = self.str[i:i+max_len]
                dup = test(sub_str).duplicated()
                if len(dup)==0:
                    max_str.append(sub_str)
            if len(max_str)>0 or max_len==1:
                break
            max_len -= 1
        return max_str
if __name__ == "__main__":
    b = test("Helloadsfworldddasrrlcxvmyadsfworl").nonrepeated()
    print(b)
