# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

import unittest
from Class.inheritance1 import *


class  GetLengthTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = GetLength()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_getLength(self):
        #object instantiation
        myDNA = DNA("ATCT")
        #access the method
        myDNA.getDNA()
        myDNA.getLength()
        
        #object instantiation
        myRNA = RNA("AUCUU")
        #access the method
        myRNA.getRNA()
        myRNA.getLength()
        

if __name__ == '__main__':
    unittest.main()

