from unittest import TestCase
from ddt import data, ddt, unpack
from sliding_window import SlidingWindow as sw

@ddt
class TestSlidingWindow(TestCase):

    @data(
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3],
        ["",0],
        ["a", 1],
        ["au", 2]
    )
    @unpack
    def test_lengthOfLongestSubstring(self, s, expect_res):
        res = sw().lengthOfLongestSubstring(s)
        # print(res)
        assert res == expect_res

    @data(
        [[90,2,40,6,10,3,23,12], 2, []],
        [[],4, []],
        [[3],1, [3]],
        [[1,3],2, [1,3]],
    )
    @unpack
    def test_max_sum_subarray(self, data, size, expect):
        res = sw().max_sum_subarray(data,size)
        print(res)
