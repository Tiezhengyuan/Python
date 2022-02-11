from copy import deepcopy
from unittest import TestCase, skip
from ddt import ddt, data, unpack
from binary_tree_next import BinaryTreeNext, TreeNode

TREE1 = TreeNode(1, 
    TreeNode(2, TreeNode(4), TreeNode(5)), \
    TreeNode(3, TreeNode(6), TreeNode(7))
)

@ddt
class TestBinaryTreeNext(TestCase):
    def setUp(self):
        self.tree = BinaryTreeNext()

    @data(
        [deepcopy(TREE1)]
    )
    @unpack
    def test_connect(self,data):
        res = self.tree.connect(data)
        print(res.val, res.left)
        p = self.tree.scan(res)
        print(p)