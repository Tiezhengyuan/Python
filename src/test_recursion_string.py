from unittest import TestCase
from ddt import ddt, data, unpack
from recursion_string import RecursionString as Recur

@ddt
class TestRecursionSimple(TestCase):
    def setUp(self):
        self.recur = Recur()

    @data(
        ["Hello", 'olleH'], ["", ""], ['a', 'a']
    )
    @unpack
    def test_reverse_str(self,data, expect):
        res = self.recur.reverse_str(data)
        # print(res)
        assert res == expect


    @data(
        ["Hello", 'o', 1], ["Hello", 'w', 0], 
        ["attat", 't', 3], ["", 'o', 0], 
    )
    @unpack
    def test_count_instance(self,data, target, expect):
        res = self.recur.count_instance(data, target)
        # print(res)
        assert res == expect
    
    @data(
        ['racecar', True],
        ['abccba', True],
        ['abcba', True],
        ['', False],
        ['abc', False],
    )
    @unpack
    def test_is_palindrome1(self, data, expect):
        res1 = self.recur.is_palindrome1(data)
        assert res1 == expect
        res2 = self.recur.is_palindrome(data)
        assert res2 == expect
    

    @data(
        ["cabccbad", [(1,6, "abccba")]],
        ["cabcbcbad", [(1,7, "abcbcba")]],
        ["aba", [(0,2, "aba")]],
        ["abba", [(0,3, "abba")]],
        ["", []],
        ["a", []],
        ["ab", []],
        ["aa", []],
        ["GCCATGTACGCGTCGAGCATGTACAAGACGGGGCC",
            [(2,8, "CATGTAC"), (17, 23, 'CATGTAC')]],
    )
    @unpack
    def test_detect_palindrome(self, data, expect):
        res = self.recur.detect_palindrome(data, 3)
        print(res)
        assert res == expect