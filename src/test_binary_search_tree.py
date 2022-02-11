from copy import deepcopy
from unittest import TestCase
from ddt import ddt, data, unpack
from binary_search_tree import BinarySearchTree as Tree
from binary_search_tree import TreeNode

TREE1 = TreeNode(50, 
    TreeNode(25, TreeNode(10, TreeNode(4), TreeNode(11)), \
        TreeNode(33, TreeNode(30), TreeNode(40))),
    TreeNode(75, TreeNode(56, TreeNode(52), TreeNode(61)), \
        TreeNode(89, TreeNode(82)))
)


@ddt
class TestRecursionSimple(TestCase):
    def setUp(self):
        self.tree = Tree()

    @data(
        [deepcopy(TREE1), 75, True],
        [deepcopy(TREE1), 50, True],
        [deepcopy(TREE1), 4, True],
        [deepcopy(TREE1), 100, False],
        [None, 3, False],
        [TreeNode(4), 4, True],
    )
    @unpack
    def test_search(self, data, val, expect):
        res = self.tree.search(data, val)
        # print(res)
        assert res == expect

    @data(
        [deepcopy(TREE1), 14],
        [deepcopy(TREE1.left), 7],
        [TreeNode(10), 1],
        [None, 0],
    )
    @unpack
    def test_count_subtree(self, data, expect):
        res = self.tree.count_subtree(data)
        print(res)
        assert res == expect


    @data(
        [deepcopy(TREE1), 75, 3],
        [deepcopy(TREE1), 50, 7],
        [deepcopy(TREE1), 4, 1],
        [deepcopy(TREE1), 100, -1],
        [None, 3, -1],
        [TreeNode(4), 4, -1],
    )
    @unpack
    def test_search_index(self, data, val, expect):
        res = self.tree.search_index(data, val)
        # print(res)
        # assert res == expect


    @data(
        [deepcopy(TREE1), 0, [0, 4, 10, 11, 25, 30, \
            33, 40, 50, 52, 56, 61, 75, 82, 89]],
        [deepcopy(TREE1), 100, [4, 10, 11, 25, 30, \
            33, 40, 50, 52, 56, 61, 75, 82, 89, 100]],
        [deepcopy(TREE1), 31, [4, 10, 11, 25, 30, 31,\
            33, 40, 50, 52, 56, 61, 75, 82, 89]],
        [TreeNode(10), 10, [10, 10]],
        [TreeNode(10), 13, [10, 13]],
        [None, 0, [0]],
    )
    @unpack
    def test_insert(self, data, val, expect):
        root = self.tree.insert(data, val)
        res = self.tree.toList(root)
        #print(res)
        assert res == expect


    @data(
        [deepcopy(TREE1)]
    )
    @unpack
    def test_scan(self, data):
        res = self.tree.scan(data)
        assert res == None


    @data(
        [deepcopy(TREE1), [4, 10, 11, 25, 30, \
            33, 40, 50, 52, 56, 61, 75, 82, 89]],
        [TreeNode(10), [10]],
        [None, []],
    )
    @unpack
    def test_toList(self, data, expect):
        res = self.tree.toList(data)
        #print(res)
        assert res == expect




    @data(
        [deepcopy(TREE1), 75, [4, 10, 11, 25, 30, \
            33, 40, 50, 52, 56, 61, 82, 89]],
        [deepcopy(TREE1), 4, [10, 11, 25, 30, \
            33, 40, 50, 52, 56, 61, 75, 82, 89]],
        [deepcopy(TREE1), 50, [4, 10, 11, 25, 30, \
            33, 40, 52, 56, 61, 75, 82, 89]],
    )
    @unpack
    def test_delete(self, data, val, expect):
        root = self.tree.delete(data, val)
        res = self.tree.toList(root)
        #print(res)
        assert res == expect