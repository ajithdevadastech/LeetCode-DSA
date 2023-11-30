# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    s = None
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        1. initialize public s to 0
        2. navigate through nodes with flag L & R
        3. if node is a leaf and flag is L, add to sum
        4. return s
        """
        s = 0
        self.s = 0

        def helper(node, flag):
            if node.left is None and node.right is None and flag == 'L':
                self.s = self.s + node.val
            if node.left:
                helper(node.left, 'L')
            if node.right:
                helper(node.right, 'R')


        helper(root, None)
        s = self.s
        self.s = None

        return s

o = Solution()

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)

n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

print(o.sumOfLeftLeaves(n3))

