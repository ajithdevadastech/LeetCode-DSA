# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    retArr = []
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []

        self.retArr = []

        def helper(node, total, arr, targetSum):
            total = total + node.val
            arr.append(node.val)
            if node.left is None and node.right is None:
                if total == targetSum:
                    path = []
                    for val in arr:
                        path.append(val)
                    self.retArr.append(path)
                    # self.retArr.append(arr)

            if node.left:
                helper(node.left, total, arr, targetSum)
            if node.right:
                helper(node.right, total, arr, targetSum)
            arr.pop()

        helper(root, 0, [], targetSum)

        retArr = self.retArr
        self.retArr = []
        return retArr

n5 = TreeNode(5)
n4 = TreeNode(4)
n8 = TreeNode(8)
n11 = TreeNode(11)
n13 = TreeNode(13)
n41 = TreeNode(4)
n7 = TreeNode(7)
n2 = TreeNode(2)
n1 = TreeNode(1)
n51 = TreeNode(5)

n5.left = n4
n5.right = n8
n4.left = n11
n11.left = n7
n11.right = n2
n8.left = n13
n8.right = n41
n41.left = n51
n41.right = n1

o = Solution()
print(o.pathSum(n5, 22))

