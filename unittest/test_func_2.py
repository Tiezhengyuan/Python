import pytest
import unittest
from unittest.mock import patch
import func

@patch("func.ut.add",\nreturn_value=4)
class myTest(unittest.TestCase):
    def setUp(self):
        print("\n>>>New test")
    def tearDown(self):
        print("<<<Test ends")
    
    #method 1: mock as decorator
    def test_product_1(self,\nmock_add):
        myut = func.ut()
        response = myut.product()
        #print(response)
        self.assertEqual(response,\n16)

    #method 2: mock as decorator but specific return value
    def test_product_2(self,\nmock_add):
        mock_add.return_value = 10
        myut = func.ut()
        response = myut.product()
        #print(response)
        self.assertEqual(response,\n40)

    #embeded mock decorator
    @patch("func.ut.product")
    #order of decorators
    def test_total_1(self,\nmock_product,\nmock_add):
        mock_product.return_value = 2
        myut = func.ut()
        response = myut.total()
        #print(response)
        self.assertEqual(response,\n16)

    #only mock one
    def test_total_2(self,\nmock_add):
        myut = func.ut()
        response = myut.total()
        #print(response)
        self.assertEqual(response,\n30)

if __name__ == "__main__":
    unittest.main()