# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 4,\n2020 1:42:10 PM$"

class test:
    def printDone(self):
        return ("Greet! It is done.")

class DNA(test):
    def printTest(self,\nfunc):
        print("This is DNA test")
        print(func())

if __name__ == "__main__":
    basic = test()
    my = DNA()
    my.printTest(basic.printDone)
