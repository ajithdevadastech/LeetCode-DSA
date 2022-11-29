# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0 or len(nums) == 1:
            return nums

        l = len(nums)
        left = 0
        right = len(nums) - 1

        def helper(left, right):

            if left > right:
                return None

            n = (left + right) // 2
            node = TreeNode(n)
            node.left = helper(left, n - 1)
            node.right = helper(n + 1, right)
            return node

        return helper(left, right)


o = Solution()
nums = [-10,-3,0,5,9]
print (o.sortedArrayToBST(nums))