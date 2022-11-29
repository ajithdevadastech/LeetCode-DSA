# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        def helper(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val <> right.val:
                return False
            helper(left.left, right.right)
            helper(left.right, right.left)

        return helper(root.left, root.right)