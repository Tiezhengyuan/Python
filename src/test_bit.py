from copy import deepcopy
from unittest import TestCase
from ddt import ddt, data, unpack
from bit import Bit

@ddt
class TestBit(TestCase):
    def setUp(self):
        self.solution = Bit()
    
    @data(
        [ 4, True ],
        [ 0, False ],
        [ 10, False ],
    )
    @unpack
    def test_isPowerOfTwo(self, data, expect):
        res = self.solution.isPowerOfTwo(data)
        # print(res)
        assert res == expect


    @data(
        [20, 2], [15, 4], [4, 1], [0, 0]
    )
    @unpack
    def test_countOnes(self, data, expect):
        res = self.solution.countOnes(data)
        # print(res)
        assert res == expect

    @data(
        [10, 8], [120, 64], [345, 256],
        [0,None], [1,None]
    )
    @unpack
    def test_largestPowerOfTwo(self, data, expect):
        res = self.solution.largestPowerOfTwo(data)
        # print(res)
        assert res == expect


    @data(
        [23, 29], [0,0], [1,1], [100, 19]
    )
    @unpack
    def test_reverseBits(self, data,expect):
        res = self.solution.reverseBits(data)
        # print(bin(data), bin(res), res)
        assert res == expect