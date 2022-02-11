from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.value = val
        self.left = left
        self.right = right

class BinaryTree:
    def scan_BFS(self, root):
        """
        convert tree to list by breadth-first search
        """
        if not isinstance(root, TreeNode):
            return []
        values = []
        pool = [root]
        while(pool):
            node = pool.pop(0)
            if node is not None:
                values.append(node.value)
                pool.append(getattr(node, 'left', None))
                pool.append(getattr(node, 'right', None))
            else:
                values.append(None)
        values = self.removeTailNone(values)
        return values

    def scan_DFS_preorder(self, root):
        """
        convert tree to list by deepth-first search
        root->left->right
        """
        if not isinstance(root, TreeNode):
            return []
        return [root.value]+ self.scan_DFS_preorder(root.left) \
            + self.scan_DFS_preorder(root.right)
        
    def scan_DFS_inorder(self, root):
        """
        convert tree to list by deepth-first search
        left->root->right
        """
        if not isinstance(root, TreeNode):
            return []
        return self.scan_DFS_inorder(root.left) + [root.value]\
            + self.scan_DFS_inorder(root.right)

    def scan_DFS_postorder(self, root):
        """
        convert tree to list by deepth-first search
        left->right->root
        """
        if not isinstance(root, TreeNode):
            return []
        return self.scan_DFS_postorder(root.left) + \
            self.scan_DFS_postorder(root.right) + [root.value]


    def removeTailNone(self, values: List) -> List:
        if len(values)>0 and values[-1] is None:
            return self.removeTailNone(values[:-1])
        else:
            return values

    def ListToTree(self, values: List[int]):
        if values ==[]:
            return None
        val = values.pop(0)
        root = TreeNode(val)
        tree_queue = [root]
        while values:
            node = tree_queue.pop(0)
            val_left = values.pop(0)
            #print(f"{node.value}->{val_left}", end=' ')
            if val_left is not None:
                node.left = TreeNode(val_left)
                tree_queue.append(node.left)
            if values:
                val_right = values.pop(0)
                if val_right is not None:
                    node.right = TreeNode(val_right)
                    tree_queue.append(node.right)
                #print(f"-{val_right}", end='\n')
        return root



    def treeToList(self, root: TreeNode):
        values = []
        pool = [root]
        while pool:
            node = pool.pop(0)
            if node is None:
                values.append(node)
            else:
                values.append(node.value)
                # print(f"{node.value}", end='\t')
                if node.value is not None:
                    if node.left:
                        pool.append(node.left)
                    else:
                        pool.append(None)
                    if node.right:
                        pool.append(node.right)
                    else:
                        pool.append(None)
            # print(values)
        return self.removeTailNone(values)

    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        if t1 is None and t2 is None: return None
        if t1 is None: return t2
        if t2 is None: return t1
        t = TreeNode(t1.value + t2.value);
        t.left = self.mergeTrees(t1.left, t2.left);
        t.right = self.mergeTrees(t1.right, t2.right);
        return t



