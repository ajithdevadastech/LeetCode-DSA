class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def PreOrderTraversal(self, root):

        if root:
            print(root.val)
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

o = Solution()
#print(o.PreOrderTraversal(root))

root = TreeNode(10)
root.left = TreeNode(7)
root.right = TreeNode(13)
root.left.left = TreeNode(4)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(16)

print(o.PreOrderTraversal(root))
