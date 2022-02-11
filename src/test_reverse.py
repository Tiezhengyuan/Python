import unittest
from ddt import ddt, data, unpack
from reverse import Reverse as R
from pytest import *

@ddt
class TestReverse(unittest.TestCase):

    @data(
        [["h","e","l","l","o"], ["o","l","l","e","h"]],
        [[],[]],
        [["a"],["a"]],
        [["a", "b"],["b", "a"]]
    )
    @unpack
    def test_reverseString(self, data, expect_res):
        R().reverseString(data)
        #print(data)
        assert data == expect_res

    
    @data(
        ["Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"]
    )
    @unpack
    def test_reverseWords(self, data, expect_res):
        res = R().reverseWords(data)
        print(res)