from unittest import TestCase
from ddt import ddt, data, unpack
from recursion_list import RecursionList as Recur


@ddt
class TestRecursionSimple(TestCase):
    def setUp(self):
        self.recur = Recur()

    @data(
        [[3,57,7,200], 267], [[], None], [[1],1]
    )
    @unpack
    def test_sum_list(self,data, expect):
        res = self.recur.sum_list(data)
        # print(res)
        assert res == expect


    @data(
        [['a', 'ab', 'abc'], ['A', 'AB', 'ABC']], 
        [[],[]], [['a'],['A']],
    )
    @unpack
    def test_capitalize_list(self,data, expect):
        res = self.recur.capitalize_list(data)
        # print(res)
        assert res == expect


    @data(
        [ [1,[3,4],[],5, [6,[7],[9,[],10,[12,34]]]],
            [1,3,4,5,6,7,9,10,12,34]],
        [ [[0,[[[[1]]]]]], [0,1]], [[],[]]
    )
    @unpack
    def test_flatten_list(self,data, expect):
        res = self.recur.flatten_list(data)
        # print(res)
        assert res == expect


    @data(
        [[3,57,7,200], [200,7,57,3]],
        [[1,2,3,4,5],[5,4,3,2,1]],
        [[],[]], [[1],[1]]
    )
    @unpack
    def test_reverse_list(self,data, expect):
        res = self.recur.reverse_list(data)
        # print(res)
        assert res == expect


    @data(
        [["ab","c","def", "ghij"], 10],
    )
    @unpack
    def test_count_list(self,data, expect_res):
        res = self.recur.count_list(data)
        # print(res)
        assert res ==expect_res



    @data(
        [[0,6,4,3,6,5], [0, 3, 4, 5, 6, 6] ],
        [[], []], [[2,2,2], [2,2,2]]
    )
    @unpack
    def test_sort_ascending(self,data, expect_res):
        self.recur.sort_ascending(data)
        # print(data)
        assert data ==expect_res

    @data(
        [[],3, [3]],  
        [[6],3, [3,6]],
        [[2],3,[2,3]],
        [[2,6],3,[2,3,6]],
        [[1,2,3,4,6,6],3, [1,2,3,3,4,6,6]],
    )
    @unpack
    def test_insert_sorted(self, data, val, expect_res):
        res=self.recur.insert_sorted(data, val)
        # print(res)
        assert res ==expect_res   

    
    @data(
        [[1,3,6,8], 3, 1],
        [[1,3,6,8], 1, 0],
        [[1,3,6,8], 8, 3],
        [[1,3,6,8], -8, -1],
        [[1,3,6,8], 2, -1],
        [[1,3,6,8], 10, -1],
        [[],3,-1],
        [[3],3,0],
        [[0,0,0,1,1,1,1,1,1,1,1,2,2,2],1,3],
        [[0,0,0,0,0,0,1,1],0,0],
    )
    @unpack
    def test_search_value(self, data, target, expect):
        res = self.recur.search_value(data,target)
        print(res)
        assert res == expect