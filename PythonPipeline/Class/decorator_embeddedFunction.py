# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 4,\n2020 2:42:05 PM$"

class test:
    def __init__(self,\ncounts):
        self.counts=counts
        
    def calcRate(self):
        ##embed a function
        def convertCounts(counts):
            return counts*3
        #calculate rate
        rate=convertCounts(self.counts)+10
        return rate
    

if __name__ == "__main__":
    print(test(30).calcRate())
