# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    parent = None
    level = None
    iscousin = False

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        iscousin = None
        def helper(node, l):
            if node.left:
                if node.left.val == x or node.left.val == y:
                    if self.parent is None:
                        self.parent = node
                        self.level = l+1
                    else:
                        if node != self.parent and l+1 == self.level:
                            self.iscousin = True
                            return
            if node.right:
                if node.right.val == x or node.right.val == y:
                    if self.parent is None:
                        self.parent = node
                        self.level = l+1
                    else:
                        if node != self.parent and l+1 == self.level:
                            self.iscousin = True
                            return
            if node.left:
                helper(node.left, l+1)
            if node.right:
                helper(node.right,l+1)

        helper(root, 0)

        self.parent = None
        self.level = None
        iscousin = self.iscousin
        self.iscousin = None

        return iscousin

#tree

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.right = n4
n3.right = n5

#fun call

o = Solution()
print(o.isCousins(n1, 5, 4))






