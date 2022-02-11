from copy import deepcopy
from unittest import TestCase, skip
from ddt import ddt, data, unpack
from binary_tree import BinaryTree as S
from binary_tree import TreeNode

TREE1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), \
    TreeNode(5, TreeNode(9), TreeNode(10))), \
    TreeNode(3, TreeNode(6, None, TreeNode(11)), \
    TreeNode(7, TreeNode(12), TreeNode(13)))
)
TREE2 = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(7))))
TREE3 = TreeNode(2, None, TreeNode(4, None, \
    TreeNode(6, None, TreeNode(8))))

@ddt
class TestBinaryTree(TestCase):



    @data(
        [TREE1, [1, 2, 3, 4, 5, 6, 7, 8, \
            None, 9, 10, None, 11, 12, 13]],
        [TREE2, [1, 3, None, 5, None, 7]],
        [TREE3, [2, None, 4, None, 6, None, 8]],
        [None, []],
        [TreeNode(3), [3]],
    )
    @unpack
    def test_scan_tree1(self, data, expect):
        """
        """
        res = S().scan_BFS(data)
        # print(res)
        assert res == expect


    @data(
        [TREE1, [1, 2, 4, 8, 5, 9, 10,\
            3, 6, 11, 7, 12, 13]],
        [TREE2, [1, 3, 5, 7]],
        [TREE3, [2, 4, 6, 8]],
        [None, []],
        [TreeNode(3), [3]],
    )
    @unpack
    def test_scan_tree2(self, data, expect):
        """
        """
        res = S().scan_DFS_inorder(data)
        # print(res)
        # assert res == expect


    @skip("na")
    @data(
        [ [6,2,8,1,4,None,None,None,None,1,None], 6],
        [[], None],
    )
    @unpack
    def test_list_to_tree(self, data, root_val):
        """
        """
        res = S().ListToTree(data)
        #print(res)
        assert getattr(res, 'val', None) == root_val

    @skip("na")
    @data(
        [ [6,2,8,1,4,5] ], #complete tree
        [ [6,None,2,8,1,None,None,4,5] ],
        [ [4] ], #no branch
        [ [1,2,None,3] ], #left bias
        [ [1,2,None,3, None, None, None] ], #left bias
        [ [1,None,2,None,3] ], #right bias
    )
    @unpack
    def test_tree_to_list(self, data):
        root_node = S().ListToTree(deepcopy(data))
        res = S().treeToList(root_node)
        #print(res)
        assert res == data


    @skip("na")
    @data(
        [[1,None,None,None], [1]],
        [[1,None,None,4,None], [1,None,None,4]],
        [[],[]],
        [[1],[1]],
        [[None, None],[]],
    )
    @unpack
    def test_removeTailNone(self,data,expect_res):
        res = S().removeTailNone(data)
        # print(res)
        assert res == expect_res


    @data(
        [ [1,3,2,5], [2,1,3,None,4,None,7], [3,4,5,5,4,None,7] ],
        [[1],[1,2], [2,2]],
        [[],[1],[1]],
        [[],[],[]],
        [[1,2,None,3], [1,None,2,None,3], [2,2,2,3,None,None,3]],
        [[1,3,None,5,None,7],[2,None,4,None,6,None,8],[]]
    )
    @unpack
    def test_mergeTrees(self, tree1, tree2, tree3):
        root1 = S().ListToTree(tree1)
        root2 = S().ListToTree(tree2)
        root3 = S().mergeTrees(root1, root2)
        res = S().treeToList(root3)
        # print('merge:', res)
        #assert res == tree3
