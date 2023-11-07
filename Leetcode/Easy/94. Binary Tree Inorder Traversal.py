# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        r = []

        def helper(node, r):
            if node is None:
                return
            if node.left is not None:
                helper(node.left, r)
            r.append(node.val)
            if node.right is not None:
                helper(node.right, r)

        helper(root, r)
        return r


o = Solution()

n3 = TreeNode(3)
n1 = TreeNode(1)
n2 = TreeNode(2)

n3.left = n1
n1.right = n2

print(o.inorderTraversal(n3))

