# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        self.dictLevelSum = {}

        def helper(node, level):
            if node:
                if level in self.dictLevelSum.keys():
                    self.dictLevelSum[level] = self.dictLevelSum[level] + node.val
                else:
                    self.dictLevelSum[level] = node.val
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)


        helper(root, 1)
        #fetch min val from dictLevelSum
        r = 1
        maxval = root.val
        for i in self.dictLevelSum.keys():
            if self.dictLevelSum[i] > maxval:
                r = i
                maxval = self.dictLevelSum[i]

        self.dictLevelSum = None
        return r

n1 = TreeNode(1)
n7 = TreeNode(7)
n0 = TreeNode(0)
n7a = TreeNode(7)
n8 = TreeNode(-8)

n1.left = n7
n1.right = n0
n7.left = n7a
n7.right = n8

o = Solution()
print(o.maxLevelSum(n1))


