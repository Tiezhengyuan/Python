from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class BinaryTreeNext:
    def connect(self, root):
        """
        Populate Next Right Pointers in Each Node
        """
        if root is None:
            return None
        else:
            if root.next:
                print(root.val, root.next.val)
            else:
                print(root.val, root.next)
            if root.next:
                if root.right:
                    root.right.next = self.getNextRight(root)
                    if root.left:
                        root.left.next = root.right
                else:
                    if root.left:
                        root.left.next = self.getNextRight(root)
            else:
                if root.left and root.right:
                    root.left.next = root.right
            self.connect(root.left)
            self.connect(root.right)
            return root

    
    def getNextRight(self, node):
        """
        if the node has nextRight and child-right node,
        return the next node of that child-right node
        """
        if node.next is not None:
            next_node = node.next
            if next_node.left:
                return next_node.left
            if next_node.right:
                return next_node.right
            if next_node.next:
                return self.getNextRight(next_node.next)
        return None
    
    def scan(self, node):
        if node is None:
            return []
        else:
            print('scan:', node.val)
            if node.next:
                return [node.val] + self.scan(node.next)
            elif node.left:
                return [node.val] + self.scan(node.left)
            elif node.right:
                return [node.val] + self.scan(node.right)
            return []