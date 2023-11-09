# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    d = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        ldepth = 1
        rdepth = 1

        def maxdepth(node, d):
            if node is None:
                if d > self.d:
                    self.d = d
                return
            maxdepth(node.left, d + 1)
            maxdepth(node.right, d + 1)

        maxdepth(root.left, ldepth)
        ldepth = self.d
        self.d = 0

        rdepth = maxdepth(root.right, rdepth)
        rdepth = self.d
        self.d = 0

        return ldepth + rdepth - 2

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

o = Solution()
print(o.diameterOfBinaryTree(n1))



