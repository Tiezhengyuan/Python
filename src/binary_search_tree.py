from typing import List

class TreeNode:
    def __init__(self, val, left=None, right=None, \
        left_size = 0, right_size = 0):
        self.value = val
        self.left = left
        self.right = right
        self.left_size = left_size
        self.left_size = right_size
        self.count = 1

class BinarySearchTree:

    def search(self, root, val):
        if not isinstance(root, TreeNode):
            return False
        else:
            if root.value == val:
                return True
            elif root.value > val:
                return self.search(root.left, val)
            return self.search(root.right, val)

    def search_index(self, node, val):
        if not isinstance(node, TreeNode):
            return -1
        else:
            if node.value == val:
                counts = self.count_subtree(node.left)
                if counts > 0: counts +=1
                return counts
            elif node.value > val:
                return self.search_index(node.left, val)
            return self.search_index(node.right, val)
    
    def count_subtree(self, node):
        counts = 0
        if isinstance(node, TreeNode):
            pool = [node]
            while pool: 
                n = pool.pop(0)
                # print('#', n.value)
                counts += 1
                if n.left:
                    pool.append(n.left)
                if n.right:
                    pool.append(n.right)
        return counts


    def insert(self, root, val):
        """
        insert value into a tree
        """
        if not isinstance(root, TreeNode):
            return TreeNode(val)
        else:
            if val == root.value:
                root.count += 1
                return root
            elif val < root.value:
                root.left = self.insert(root.left, val)
            else:
                root.right = self.insert(root.right, val)
        return root
    
    def delete(self, node, val):
        """
        delete value from a tree
        """
        #search the node that should be deleted
        if node is None:
            return None
        elif val < node.value:
            node.left = self.delete(node.left, val)
            return node
        elif val > node.value:
            node.right = self.delete(node.right, val)
            return node
        elif val == node.value:
            #either or both of left-right is none
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            #Both of left and right exist
            # print('#', node.value, val)
            node.right = self.liftValue(node.right, node)
            return node
    
    def liftValue(self, nodeRight, nodeDel):
        """
        update value of nodeDel
        """
        # print(nodeRight.value, nodeDel.value)
        #walk through the most left path
        if nodeRight.left:
            nodeRight.left = self.liftValue(nodeRight.left, nodeDel)
            return nodeRight
        #return the most left end node
        else:
            nodeDel.value = nodeRight.value
            return nodeRight.right

    def scan(self, root):
        """
        print value from most inner to the root,
        and from left to right
        """
        if root is not None:
            self.scan(root.left)
            #print(root.value)
            self.scan(root.right)


    def toList(self, node):
        if node is None:
            return []
        else:
            value = [node.value] * node.count
            return self.toList(node.left) + value +\
                self.toList(node.right)

    # def fromList(self, s):
