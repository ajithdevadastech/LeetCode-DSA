# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    c = None
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        1. initialize a public arr
        2. assign max = root.val
        3. navigate thru each node
        4. check if node.val > max, if yes, add to arr, max = node.val. else, move on
        
        """

        c = 0
        self.c = 0

        m = root.val

        def helper(node, max):
            mx = max
            if node.val >= max:
                self.c = self.c + 1
                mx = node.val
            if node.left:
                helper(node.left, mx)
            if node.right:
                helper(node.right, mx)

        helper(root, m)
        c = self.c
        self.c = None
        return c

o = Solution()

na = TreeNode(3)
nb = TreeNode(1)
nc = TreeNode(4)
nd = TreeNode(3)
ne = TreeNode(1)
nf = TreeNode(5)

na.left = nb
na.right = nc
nb.left = nd
nc.left = ne
nc.right = nf

print(o.goodNodes(na))