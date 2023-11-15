# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    dictLevelNodes = {}

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            self.dictLevelNodes = {}
            return []
        if root.left is None and root.right is None:
            self.dictLevelNodes = {}
            return [[root.val]]

        r = []

        self.dictLevelNodes[0] = [root.val]

        dictLevelNodes = {}

        def helper(node, level):
            if node is None:
                return
            if node.left or node.right:
                level = level + 1

                if node.left:
                    if level in self.dictLevelNodes.keys():
                        self.dictLevelNodes[level].append(node.left.val)
                    else:
                        self.dictLevelNodes[level] = [node.left.val]
                    helper(node.left, level)

                if node.right:
                    if level in self.dictLevelNodes.keys():
                        self.dictLevelNodes[level].append(node.right.val)
                    else:
                        self.dictLevelNodes[level] = [node.right.val]
                    helper(node.right, level)

        helper(root, 0)
        dictLevelNodes = self.dictLevelNodes.copy()
        self.dictLevelNodes = None
        for i in dictLevelNodes.keys():
            r.append(dictLevelNodes[i])
        return r

o = Solution()

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)
n6 = TreeNode(6)
n10 = TreeNode(10)

n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7
n9.left = n6
n9.right = n10

print(o.levelOrder(n3))




