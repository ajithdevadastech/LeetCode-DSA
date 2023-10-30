# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    c = 0
    r = None
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(node):
            if node.left is not None:
                helper(node.left)
            self.c = self.c + 1
            if self.c == k:
                self.r = node.val
                return
            if node.right is not None:
                helper(node.right)

        helper(root)
        return self.r



N1 = TreeNode(3)
N2 = TreeNode(1)
N3 = TreeNode(4)
N4 = TreeNode(2)

N1.left = N2
N1.right = N3

N2.right = N4

o = Solution()
root = N1
k = 1
print(o.kthSmallest(root, k))


