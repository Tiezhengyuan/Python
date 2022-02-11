import unittest
from ddt import ddt, data, unpack
from binary_search import BinarySearch as BS
from pytest import *

@ddt
class TestBinarySearch(unittest.TestCase):

    @unittest.skip("skipping test")
    @data(
        #generate new mid==11
        [0,None,23, 0,11,23],
        #mid==11 is big in 0-23. select 0-10
        [0,-11,23, 0,5,11],
        #mid==5 is small in 0-10. select 6-10
        [0,5,10, 6,8,10],
        [0,-5,10, 0,2,5],
        [0,-1,1, 0,0,1],
        [0,0,1, 0,None,1],
        [0,None,1, 0,0,1],
        [18,18,19, 19,None,19],
        #wrong L,M,R
        [18,18,18, 18,None,18], #L<R
        [18,19,19, 20,None,19], #M<R
        [0,1,1, 2,None,1], #M<R
        [0,-1,0, 0,None,0], #L<R, M>=L
        [0,0,0, 0,None,0], #L<R
        [0,1,0, 0,None,0], #M<R, L<R
        [0,None,0, 0,None,0] #L<R
    )
    @unpack
    def test_get_mid_1(self, L,M,R, eL,eM,eR):
        rL, rM, rR = BS().get_mid(L,M,R)
        #print(rL, rM, rR)
        assert rL == eL
        assert rM == eM
        assert rR == eR
    
    
    @unittest.skip("skipping test")
    @data(
        [0,23, [11, 17, 20, 22, None]],
        [0,24,  [12, 18, 21, 23, None]],
        [12,13, [12, None]],
        [0,1, [0, None]],
        [12,12, [None]],
        [2,1, [None]]
    )
    @unpack
    def test_get_mid_2(self, L, R, expect_mid):
        M, res = None, []
        while True:
            L, M, R = BS().get_mid(L,M,R)
            res.append(M)
            if M is None: break
        #print(res)
        assert res == expect_mid

    @unittest.skip("skipping test")
    @data(
        [0,23, [11, 5, 2, 1, 0, None]],
        [0,48, [24, 12, 6, 3, 1, 0, None]],
        [10,12, [11,10,None]],
        [0,1, [0, None]],
        [0,0, [None]],
        [12,12, [None]],
        [12,13, [12, None]]
    )
    @unpack
    def test_get_mid_3(self, L, R, expect_mid):
        M, res = None, []
        while True:
            if M is not None and M >0:
                M = -M
            L, M, R = BS().get_mid(L,M,R)
            res.append(M)
            if M is None: break
        #print(res)
        assert res == expect_mid


    @unittest.skip("skipping test")
    @data(
        [[-1,0,3,5,9,12], -1, 0],
        [[-1,0,3,5,9,12], 9, 4],
        [[-1,0,3,5,9,12], 12, 5],
        [[-1,0,3,5,9,12], 20, -1],
        [[-1,0,3,5,9,12], -20, -1],
        [[2,7,11,15], 2, 0],
        [[3], 3, 0],
        [[3], -3, -1],
        [[], 4, -1],
        [[2,2, 7,11,15], 2, 1]
    )
    @unpack
    def test_search(self, nums, target, expect_res):
        res = BS().search(nums, target)
        #print(res)
        assert res == expect_res

    @unittest.skip("skipping test")
    @data(
        [[-1,0,3,5,9,12], -1, 0],
        [[-1,0,3,5,9,12], 9, 4],
        [[-1,0,3,5,9,12], 12, 5],
        [[-1,0,3,5,9,12], 20, 6],
        [[-1,0,3,5,9,12], -20, 0],
        [[-1,0,3,5,9,12], 4, 3],
        [[2,7,11,15], 2, 0],
        [[2,7,11,15], 4, 1],
        [[15], 15, 0],
        [[3], -3, 0], #insert the first
        [[0,0,0,0,2],1, 4], #insertion
        [[0,0,0,0,2],0, 0], #duplicates
        [[], 4, 0], #empty
        [[0],4,1]
    )
    @unpack
    def test_search_insert(self, nums, target, expect_res):
        res = BS().search_insert(nums, target)
        #print(res)
        assert res == expect_res
    
    
    #@unittest.skip("skipping test")
    @data(
        [[2,7,11,15], 9, [1,2]],
        [[2,2,11,15], 4, [1,2]],
        [[2,3,4], 6, [1,3]],
        [[5,25,75], 100, [2,3]],
        [[0,0,3], 0, [1,2]],
        [[3,24,50,79,88,150,345], 200, [3,6]],
        [[1,2,3,4,4,9,56,90], 8, [4,5]],
        [[-1,0], -1, [1,2]]
    )
    @unpack
    def test_twoSum(self, numbers, target, expect_res):
        res = BS().twoSum(numbers, target)
        #print(res)
        assert res == expect_res