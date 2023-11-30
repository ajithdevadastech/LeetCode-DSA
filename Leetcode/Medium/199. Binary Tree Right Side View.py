# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    rdict = None
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        if root.left is None and root.right is None:
            return[root.val]


        r = []
        self.rdict = {}


        def helper(node, d):
            if d not in self.rdict.keys():
                self.rdict[d] = node.val
            if node.right:
                helper(node.right, d+1)
            if node.left:
                helper(node.left, d+1)

        helper(root, 0)
        for i in self.rdict.values():
            r.append(i)
        self.rdict = None
        return r

o = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n2.right = n5


print(o.rightSideView(n1))
