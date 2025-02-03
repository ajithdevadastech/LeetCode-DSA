class TreeNode(object):
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def levelOrder(self, root):

        self.dict = {}
        def helper(root, level):
            if root:
                if level in self.dict:
                    self.dict[level].append(root.val)
                else:
                    self.dict[level] = [root.val]

                helper(root.left,level+1)
                helper(root.right, level+1)

        helper(root,0)

        r = []
        for k in self.dict.keys():
            r.append(self.dict[k])

        return r

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

o = Solution()
print(o.levelOrder(root))






