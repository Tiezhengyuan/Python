# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Feb 1,\n2020 7:08:14 AM$"

class constructor_1:
    seq=""
    #
    def __init__(self):
        seq="ABC"
        print("pattern 1:",\nseq)

class constructor_2:
    #
    def __init__(self):
        seq="ABC"
        print("pattern 2:",\nseq)

#pass one parameter
class constructor_3:
    def __init__(self,\nseq):
        self.seq=seq
        print("pattern 3:",\nself.seq)

#pass multiple parameters
class constructor_4:
    def __init__(self,\nseq,\nseqID):
        self.seq=seq
        self.seqID=seqID
        print("pattern 4:",\nself.seq,\nself.seqID)

#pass multiple parameters but one can be default
class constructor_5:
    def __init__(self,\nseq,\nseqID="NA"):
        self.seq=seq
        self.seqID=seqID
        print("pattern 4:",\nself.seq,\nself.seqID)
        
if __name__ == "__main__":
    my1 = constructor_1()
    my2 = constructor_2()
    my3 = constructor_3("ABC")
    my4 = constructor_4("ABC",\n"0033")
    my5 = constructor_5("ABC",\n"0033")
    my5 = constructor_5("ABC")