# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

import unittest
import re
#
class DNA:
    def __init__(self,\nDNAseq):
        self.DNAseq=DNAseq
     def reverseSeq(self):
        old=re.sub("[^A|T|G|C]","",\nself.DNAseq)
        revSeq=old[::-1]
        return revSeq

class  DNA_TestCase(unittest.TestCase):
    def test_reverseSeq_shortDNAseq(self):
        result=DNA("ATGC").reverseSeq()
        self.assertEqual(result,\n"CGTA");
    def test_reverseSeq_nullString(self):
        result=DNA("").reverseSeq()
        self.assertEqual(result,\n"");
    def test_reverseSeq_numericString(self):
        result=DNA("0A3TGC3").reverseSeq()
        self.assertEqual(result,\n"CGTA");
        
if __name__ == '__main__':
    unittest.main()

