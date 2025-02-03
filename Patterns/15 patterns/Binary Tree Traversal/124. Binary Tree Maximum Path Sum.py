class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def maxPathSum(self, root):

        self.maxval = -1001
        def helper(root):
            if root:
                l = helper(root.left)
                r = helper(root.right)
                if l is None and r is not None:
                    k = max(r + root.val, root.val)
                    m = k
                elif l is not None and r is None:
                    k = max(l + root.val, root.val)
                    m = k
                elif l is not None and r is not None:
                    m = max(root.val, l + root.val, r + root.val, l + r + root.val)
                    k = max(root.val, l + root.val, r + root.val)
                else:
                    k = root.val
                    m = k
                if m > self.maxval:
                    self.maxval = m
                return k
            else:
                return None

        helper(root)
        return self.maxval


# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


#root = TreeNode(-3)

root = TreeNode(5)
root.left = TreeNode(4)
root.right= TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(-1)
root.right.left = TreeNode(-2)


o = Solution()
print(o.maxPathSum(root))



