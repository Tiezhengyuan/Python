from unittest import TestCase
from ddt import ddt, data, unpack
from recursion_dict import RecursionDict as Recur


@ddt
class test_Recursion(TestCase):
    def setUp(self):
        self.recur = Recur()

    @data(
        [{  "a": 2,  "b": 4,  "c": 5,  "d": 1,},  [2, 4, 5, 1]],
        [{},[]],
        [{'a':3.4,'b':'c'},[]],
        [{  "a": 2,  "b": {"c": {"d": 1}}},  [2, 1]],
    )
    @unpack
    def test_sum_dict(self,data,expect):
        res = self.recur.sum_dict(data)
        # print(res)
        assert res == expect