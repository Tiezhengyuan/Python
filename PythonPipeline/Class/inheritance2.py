# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

#parent class 1
class molecular:
    def __init__ (self,\nmolSeq):
        self.molSeq=molSeq
    
    #method of the parent class
    def getLength(self):
        seqLen=len(self.molSeq)
        print("The length of the sequence is",\nseqLen)
        return seqLen
    
#parent class 2
class source:
    def __init__ (self,\nspecie):
        self.specie=specie

#children class
class DNA (molecular,\nsource):
    def __init__ (self,\nmolSeq,\nspecie,\naccessionNum):
        molecular.__init__(self,\nmolSeq)
        source.__init__(self,\nspecie)
        self.accessionNum=accessionNum

    #method of the children class
    def reverseSeq(self):
        revSeq = self.molSeq[::-1]
        return revSeq

class CDS (DNA):
    def __init__ (self,\n molSeq,\nspecie,\naccessionNum,\ngeneID):
        DNA.__init__(self,\nmolSeq,\nspecie,\naccessionNum)
        self.geneID=geneID

    #method of the children class
    def exportSeq(self):
        print("\nFASTA format:")
        seqRecord = ">" + self.geneID + "|" + self.accessionNum + " " +  self.specie + "\n" + self.molSeq
        print(seqRecord)
        return seqRecord


