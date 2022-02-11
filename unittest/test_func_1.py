import pytest
import unittest
from unittest.mock import patch
import func

class myTest(unittest.TestCase):
    def setUp(self):
        print("\n>>>New test")
    def tearDown(self):
        print("<<<Test ends")
    
    #method 1: mock as decorator
    @patch("func.ut.add")
    def test_product_1(self,\nmock_add):
        mock_add.return_value = 4
        myut = func.ut()
        response = myut.product()
        #print(response)
        self.assertEqual(response,\n16)

    #method 2: mock as context manager
    def test_product_1(self):
        with patch("func.ut.add",\nreturn_value=4):
            myut = func.ut()
            response = myut.product()
            #print(response)
            self.assertEqual(response,\n16)

    #embeded mock decorator
    @patch("func.ut.add")
    @patch("func.ut.product")
    def test_total_1(self,\nmock_add,\nmock_product):
        mock_add.return_value = 4
        mock_product.return_value = 4
        myut = func.ut()
        response = myut.total()
        #print(response)
        self.assertEqual(response,\n18)

    #only mock one
    @patch("func.ut.add")
    def test_total_2(self,\nmock_add):
        mock_add.return_value = 4
        myut = func.ut()
        response = myut.total()
        #print(response)
        self.assertEqual(response,\n30)

if __name__ == "__main__":
    unittest.main()