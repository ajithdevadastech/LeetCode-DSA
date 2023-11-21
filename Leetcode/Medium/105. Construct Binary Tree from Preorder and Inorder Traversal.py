# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    i = 0
    preorder = []
    root = None

    def buildTree(self, preorder, inorder):

        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        """
        algorithm
        -------------
        
        
        if there are lefts, add preorder[next] as left child, recurse with preorder[next] node and inorder left, right
        if no left, recurse with preorder[next] and inorder right , don't do anything?
        if there are rights, add preorder[next] as right child, recurse with preorder[next] and inorder right, right
        if there are no rights, don't do anything
        
        """

        self.preorder = preorder

        def retLRarrays (val, arr):

            i = 0
            while i < len(arr):
                if arr[i] == val:
                    break
                else:
                    i = i + 1
            larr = arr[0:i]
            rarr = arr[i+1:len(arr)]

            return larr, rarr


        def helper (node, leftArr, rightArr):
            if len(leftArr) > 0:
                self.i = self.i + 1
                node.left = TreeNode(self.preorder[self.i])
                larr, rarr = retLRarrays(self.preorder[self.i], leftArr)
                helper(node.left, larr, rarr)
            if len(rightArr) > 0:
                self.i = self.i + 1
                node.right = TreeNode(self.preorder[self.i])
                larr, rarr = retLRarrays(self.preorder[self.i], rightArr)
                helper(node.right, larr, rarr)

        self.root = TreeNode(preorder[0])
        larr, rarr = retLRarrays(self.root.val, inorder)
        helper(self.root, larr, rarr)

        root = self.root
        self.root = None
        self.i = None
        self.preorder = None

        return root



o = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

r = o.buildTree(preorder, inorder)
print(r)

















        


