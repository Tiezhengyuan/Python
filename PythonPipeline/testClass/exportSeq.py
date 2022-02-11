# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

import unittest
from Class.inheritance2 import *

class  ExportSeqTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = ExportSeq()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_exportSeq(self):
        #instantiate DNA
        my = DNA("ATGCGCTAA",\n"human",\n"ACC102323")
        revSeq=my.reverseSeq()
        print("Reversed sequence is ",\nrevSeq)
        
        #instantiate CDS
        my = CDS("ATGCGCTAA",\n"human",\n"ACC102323",\n"G00344243.1")
        record=my.exportSeq()
        

if __name__ == '__main__':
    unittest.main()

