# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        dictNode = {}
        self.root = None

        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 2:
            self.root = TreeNode(preorder[0])
            self.root.left = TreeNode(preorder[1])
            return self.root

        def helper(dir,pre,post, node):

            if pre == post:
                if dir == 'R':
                    node.right = TreeNode(pre[0])
                else:
                    node.left = TreeNode(pre[0])
                return
            elif len(pre) == 0 and len(post) > 0:
                i = len(post) - 1
                while i >= 0:
                    node.left = TreeNode(post[i])
                    node = node.left
                    i = i - 1
                return
            elif len(post) > 0:
                n = TreeNode(pre[0])
                if dir == '':
                    self.root = n
                    node = n
                else:
                    if dir == 'L':
                        node.left = n
                        node = node.left
                    else:
                        node.right = n
                        node = node.right

                helper('L',pre[1:pre.index(post[-2])], post[0:post.index(pre[1])+1], node)
                helper('R', pre[pre.index(post[-2]):], post[post.index(pre[1])+1:-1], node)


        helper('',preorder, postorder, None)
        return self.root

# preorder = [1,2,4,5,3,6,7]
# postorder = [4,5,2,6,7,3,1]
preorder = [4,2,1,3]
postorder = [3,1,2,4]
o= Solution()
print(o.constructFromPrePost(preorder, postorder))




