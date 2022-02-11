from unittest import TestCase
from ddt import ddt, data, unpack
from recursion_sequence import RecursionSequence

@ddt
class TestRecursionSimple(TestCase):
    def setUp(self):
        self.recur = RecursionSequence()

    @data(
        [100, 5050], [0,0], [1,1]
    )
    @unpack
    def test_acc_add(self,data, expect):
        res = self.recur.acc_add(data)
        # print(res)
        assert res == expect


    @data(
        [1, 10, 2, 25], [0, 10, 2, 30], [-100,123,7, 272],
        #wrong input
        [10,2,3,0], [2,2,1,2],
    )
    @unpack
    def test_acc_add2(self,start,end,step, expect):
        res = self.recur.acc_add2(start,end,step)
        # print(res)
        assert res == expect


    @data(
        [10, 89], [-12, None],
    )
    @unpack
    def test_fib(self,data, expect):
        res = self.recur.fib(data)
        # print(res)
        assert res == expect


    @data(
        [10, 3628800],[1,1], [0, None],
    )
    @unpack
    def test_cal_factorial(self,data, expect):
        res = self.recur.cal_factorial(data)
        print(res)
        assert res == expect