# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

#parent class
class molecular:
    def __init__ (self,\nmolSeq):
        self.molSeq=molSeq
    
    #method of the parent class
    def getLength(self):
        seqLen=len(self.molSeq)
        print("The length of the sequence is",\nseqLen)
        return seqLen

class DNA (molecular):
    #method of the children class
    def getDNA(self):
        print("The DNA sequence is",\nself.molSeq)
        return self.molSeq

class RNA (molecular):
    #method of the children class
    def getRNA(self):
        print("The RNA sequence is",\nself.molSeq)
        return self.molSeq


