class TreeNode(object):
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def kthSmallest(self, root, k):

        self.r = None
        self.count = 0
        def helper(root):
            if root:
                helper(root.left)
                self.count = self.count + 1
                if self.count == k:
                    self.r = root.val
                helper(root.right)

        helper(root)
        return self.r


root = TreeNode(10)
root.left = TreeNode(7)
root.right = TreeNode(13)
root.left.left = TreeNode(4)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(16)

k =  4

o = Solution()
print(o.kthSmallest(root, k))





