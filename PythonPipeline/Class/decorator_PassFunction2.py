# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 4,\n2020 1:42:10 PM$"

class test:
    @classmethod
    def printDone(self,\nfunc):
        def oncall (*args):
            print("First call the function ",\nfunc.__name__)
            print("\tvalue = ",\nfunc(*args))
            print("Greet! It is done.")
        return oncall

class DNA(test):
    @test.printDone
    def printTest(self):
        print("\tThis is DNA test")
        return 1

if __name__ == "__main__":
    DNA().printTest()
