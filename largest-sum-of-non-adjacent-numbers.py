"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtreesl:

     0
    / \
   1   0
      / \
     1   0
    / \
   1   1
"""

class Node:
    """
    A Simple Class Representing a Node of a Binary Tree
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def set_data(self, data):
        self.data = data

def countUniValueSubtrees(root):
    count = 0
    if (root == None):
        return 0
    
    isUniValHelper(root, count)
    return count

def isUniValHelper(node, count):
    # Base case: if both children are null, we know the node is a univalue, we can increment count and return true
    if (node.left == None and node.right == None):
        count += 1
        return True

    # Check isUniVal for each child search tree
    isUnival = True
    if node.left != None:
        isUniVal, count = isUniValHelper(node.left) and isUniVal and node.left.data == node.val
    
    if node.right != None:
        isUniVal, count = isUniValHelper(node.right) and isUnival and node.right.data == node.val
    
    # return early if isUniVal is false
    if (not isUniVal):
        return False

    count += 1
    return True, count


root = Node(0)
Node.left = Node(1)
Node.right = Node(0)
Node.right.right = Node(0)
Node.right.left = Node(1)
Node.right.left.left = Node(1)
Node.right.left.right = Node(1)
print(countUniValueSubtrees(root))