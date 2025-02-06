class TreeNode(object):
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):

        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return[[root.val]]
            else:
                return []


        self.r = []

        def helper(root, arr, total):
            if root:
                arr.append(root.val)
                total = total + root.val
                if root.left is None and root.right is None:
                    if total == targetSum:
                        self.r.append(arr.copy())
                helper(root.left, arr, total)
                helper(root.right, arr, total)
                arr.pop()

        helper(root, [], 0)
        return self.r

o = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

targetSum = 22
print(o.pathSum(root, targetSum))
