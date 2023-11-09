# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    r = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        depth = 0

        def helper(node, d):
            if node is None:
                if d > self.r:
                    self.r = d
                return
            helper(node.left, d + 1)
            helper(node.right, d + 1)


        helper(root, depth)
        depth = self.r
        self.r = 0
        return depth

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

print(o.maxDepth(n3))