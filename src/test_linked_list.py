from copy import deepcopy
import unittest
from ddt import ddt,data,unpack
from linked_list import LinkedList, Node

example_list = LinkedList()
first, second, third = Node(1), Node(2), Node(3)
example_list.head = first
first.next, second.next = second, third

@ddt
class TestLinkedList(unittest.TestCase):

    @data(
        [deepcopy(example_list), 1, 1],
        [deepcopy(example_list), 3, 3],
        [deepcopy(example_list), 6, None],
        [LinkedList(), 1, None]
    )
    @unpack
    def test_generator(self, list2, times, expect_data):
        g = list2.gen_list()
        res = None
        for i in range(times):
            res = next(g)
            if res is None: break
        else:
            res = res.data
        #print(res)
        assert res == expect_data

    @data(
        [deepcopy(example_list), [1,2,3]]
    )
    @unpack
    def test_toList(self, list2, expect_list):
        res = list2.toList()
        #print(res)
        assert res == expect_list

    @data(
        [deepcopy(example_list), 4, [4,1,2,3]]
    )
    @unpack
    def test_addNode(self, list2, value, expect_list):
        list2.addNode(value)
        res = list2.toList()
        #print(res)
        assert res == expect_list


    @data(
        [deepcopy(example_list), 4, [1,2,3,4]]
    )
    @unpack
    def test_appendNode(self, list2, value, expect_list):
        list2.appendNode(value)
        res = list2.toList()
        #print(res)
        assert res == expect_list

    @data(
        [deepcopy(example_list), 1, 6, [1, 6, 2, 3], True],
        [deepcopy(example_list), 0, 6, [6, 1, 2, 3], True],
        [deepcopy(example_list), 3, 4, [1, 2, 3, 4], True],
        [deepcopy(example_list), 10, 6, [1, 2, 3], False],
        [LinkedList(), -1, 6, [], False],
        [LinkedList(), 0, 6, [6], True],
    )
    @unpack
    def test_insertNode(self, list2, index, value, 
        expect_list, expect_return):
        res= list2.insertNode(index, value)
        res_list = list2.toList()
        #print(res_list)
        assert res == expect_return
        assert res_list == expect_list


    @data(
        [deepcopy(example_list), 3],
        [LinkedList(), 0]
    )
    @unpack
    def test_appendNode(self, list2, expect_len):
        res = list2.getLength()
        assert res == expect_len


    @data(
        [deepcopy(example_list), 2, 3],
        [deepcopy(example_list), 0, 1],
        [deepcopy(example_list), 10, None],
        [LinkedList(), 0, None]
    )
    @unpack
    def test_getNode(self, list2, index, expect_res):
        res = list2.getNode(index)
        if res is None:
            assert res == expect_res
        else:
            assert res.data == expect_res