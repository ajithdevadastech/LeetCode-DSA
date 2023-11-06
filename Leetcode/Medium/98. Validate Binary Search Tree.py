# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower, upper):
            if node is None:
                return True
            if (lower is not None and node.val < lower) or (upper is not None and node.val > upper):
                return False
            return helper(node.left, lower, node.val-1) and helper(node.right, node.val + 1, upper)

        if helper(root, None, None) is False:
            return False
        else:
            return True

o = Solution()

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(6)
n4 = TreeNode(3)
n5 = TreeNode(7)


n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(o.isValidBST(n1))