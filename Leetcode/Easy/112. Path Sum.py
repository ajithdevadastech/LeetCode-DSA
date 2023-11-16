# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    flag = False
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum

        self.flag = False
        flag = None

        def helper(node, total, targetSum):
            total = total + node.val
            if node.left is None and node.right is None:
                if total == targetSum:
                    self.flag = True
                return
            else:
                if node.left:
                    helper(node.left, total, targetSum)
                if node.right:
                    helper(node.right, total, targetSum)

        helper(root, 0, targetSum)

        flag = self.flag
        self.flag = None
        return flag

n5 = TreeNode(5)
n4 = TreeNode(4)
n8 = TreeNode(8)
n11 = TreeNode(11)
n13 = TreeNode(13)
n41 = TreeNode(4)
n7 = TreeNode(7)
n2 = TreeNode(2)
n1 = TreeNode(1)

n5.left = n4
n5.right = n8
n4.left = n11
n11.left = n7
n11.right = n2
n8.left = n13
n8.right = n41
n41.right = n1

o = Solution()
print(o.hasPathSum(n5, 22))