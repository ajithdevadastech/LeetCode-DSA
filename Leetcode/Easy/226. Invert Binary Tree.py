# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    r = None
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.r = root

        def helper(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                return
            #swap
            k = node.left
            node.left = node.right
            node.right = k

            if node.left is not None:
                helper(node.left)
            if node.right is not None:
                helper(node.right)

        helper(root)
        ret = self.r
        self.r = None
        return ret

o = Solution()

n4 = TreeNode(4)
n2 = TreeNode(2)
n7 = TreeNode(7)
n1 = TreeNode(1)
n3 = TreeNode(3)
n6 = TreeNode(6)
n9 = TreeNode(9)

n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3
n7.left = n6
n7.right = n9

o.invertTree(n4)


