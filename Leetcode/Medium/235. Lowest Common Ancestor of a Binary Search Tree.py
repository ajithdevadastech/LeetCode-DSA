# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    lca = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.lca = root

        dictNodes = {}

        def navigatetop (node, p):
            if node is None:
                return
            dictNodes[node] = 1
            if p.val > node.val:
                navigatetop(node.right, p)
            elif p.val < node.val:
                navigatetop(node.left, p)
            else:
                return

        def helper(node, q):
            if node is None:
                return
            if node in dictNodes.keys():
                self.lca = node
            if q.val > node.val:
                helper(node.right, q)
            elif q.val < node.val:
                helper(node.left, q)
            else:
                return

        navigatetop(root, p)
        helper(root, q)
        return self.lca







o = Solution()

#tree
n1 = TreeNode(6)
n2 = TreeNode(2)
n3 = TreeNode(8)
n4 = TreeNode(0)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)
n8 = TreeNode(3)
n9 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n8
n5.right = n9
n3.left = n6
n3.right = n7

p = n5
q = n6
print(o.lowestCommonAncestor(n1, p, q).val)