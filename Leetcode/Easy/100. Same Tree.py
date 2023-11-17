# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        self.flag = True
        flag = True

        def helper(node1, node2):
            if node1 is None and node2 is None:
                return
            elif (node1 is not None and node2 is None) or (node1 is None and node2 is not None):
                self.flag = False
                return
            else:
                if node1.val != node2.val:
                    self.flag = False
                    return

            helper(node1.left, node2.left)
            helper(node1.right, node2.right)


        helper(p, q)
        flag = self.flag
        self.flag = None
        return flag

o = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n1.right = n3
n3.left = n4

n1a = TreeNode(1)
n2a = TreeNode(2)
n3a = TreeNode(3)
n4a = TreeNode(4)

n1a.left = n2a
n1a.right = n3a
n3a.right = n4a

print(o.isSameTree(n1, n1a))






