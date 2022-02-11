import pytest
import unittest
from unittest.mock import Mock,\npatch
import func


class myTest(unittest.TestCase):
    def setUp(self):
        print("\n>>>New test")
        self.mock_add = patch("func.ut.add").start()
        #self.mock_div = patch("func.ut.div").start()

    def tearDown(self):
        self.addCleanup(patch.stopall)
        print("<<<Test ends")
    
    #assert statements
    def test_div(self):
        myut = func.ut()
        #
        response = myut.div(4,2)
        self.assertEqual(response,\n2)
        
        #dominator is zero
        self.assertRaises(ZeroDivisionError,\nmyut.div,\n1,0)

        #string type
        self.assertRaises(TypeError,\nmyut.div,\n3,\n'a')

    @patch("func.divException")
    def test_div_exception(self,\nmock_exception):
        myut = func.ut()
        
        #test 1
        response = myut.div_exception(4,2)
        
        #test 2 basic exception
        #pytest.raises in a with block as context manager
        #check if exception is actually raised
        with pytest.raises(Exception) as err:
            self.assertTrue(myut.div_exception(4,0))
        response = str(err.value)
        #print(response)
        self.assertEqual(response,\n'zero')

        #test 3 external excepton
        print(mock_exception)
        mock_exception.side_effect = Exception
        with pytest.raises(Exception) as err:
            self.assertTrue(myut.div_exception(4,1))
        response = str(err.value)
        print("external exception = %s"%response)

    #method 1: mock as decorator
    def test_product(self):
        myut = func.ut()
        self.mock_add.return_value = 4
        response = myut.total2(1,2)
        #print(response)
        #self.assertEqual(response,\n16)

        #
        #self.mock_add.return_value = -4
        #mock=Mock()
        #mock.side_effect = Exception
        #response = myut.product2()
        #print(response)
        #self.assertEqual(response,\n16)

    def test_total2(self):
        pass


if __name__ == "__main__":
    unittest.main()