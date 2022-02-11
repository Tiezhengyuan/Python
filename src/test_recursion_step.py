from unittest import TestCase
from ddt import ddt, data, unpack
from recursion_step import RecursionStep as Recur

@ddt
class TestRecursionStep(TestCase):
    def setUp(self):
        self.recur = Recur()

    @data(
        [10, 5050], 
    )
    @unpack
    def test_count_steps(self,data, expect):
        res = self.recur.count_steps(data)
        # print(res)
        assert res == expect