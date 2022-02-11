# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

import unittest
from Class.new_class import *

class  GetDNATestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = GetDNA()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_getDNA(self):
        #object instantiation
        myDNA = DNA()
        #access the variable in the class
        print(myDNA.DNASeq)
        #access the method
        myDNA.getDNA()


if __name__ == '__main__':
    unittest.main()

