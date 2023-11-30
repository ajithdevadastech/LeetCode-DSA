# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        """
        algorithm
        -----------
        
        1. call helper, pass root and d = 0
        2. helper (node, depth)
        2.a if node.left is none and node.right is none, return depth
        2.b. if abs(ifnull(helper(node.left, d+1),0) - ifnull(helper(node.right, d+1),0)) > 1, set global flag to false
        
        """


        def helper(node):
            if node is None:
                return 0
            l = helper(node.left)
            r = helper(node.right)

            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            else:
                return max(l,r) + 1


        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if helper(root) == -1:
            return False
        else:
            return True


o = Solution()

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)
n6 = TreeNode(6)
n8 = TreeNode(8)

n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7
n7.left = n6
n7.right = n8

print(o.isBalanced(n3))


