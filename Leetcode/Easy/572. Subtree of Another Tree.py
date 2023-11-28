# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    flghassubroot = None
    rethassubroot = None
    flgismatching = None

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        """
        algorithm:

        find subroot inside root, if not found return False
        once found, loop through both nodes, any mismatch return False, else return True

        """

        if root.left is None and root.right is None:
            if subRoot.left is None and subRoot.right is None:
                if root.val == subRoot.val:
                    return True
                else:
                    return False

        self.flghassubroot = False
        self.flgismatching = True
        self.rethassubroot = []

        def hassubroot(r, sr):

            if r is not None:
                if r.val == sr.val:
                    self.flghassubroot = True
                    self.rethassubroot.append(r)
                hassubroot(r.left, sr)
                hassubroot(r.right, sr)


        def isMatching(node1, node2):

            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                self.flgismatching = False
            if node1 is not None and node2 is not None:
                if node1.val != node2.val:
                    self.flgismatching = False
                else:
                    isMatching(node1.left, node2.left)
                    isMatching(node1.right, node2.right)

        hassubroot(root, subRoot)

        if self.flghassubroot:
            for node in self.rethassubroot:
                self.flgismatching = True
                isMatching(node, subRoot)
                if self.flgismatching:
                    break
        else:
            return False

        flgismatching = self.flgismatching

        self.flghassubroot = None
        self.rethassubroot = None
        self.flgismatching = None

        return flgismatching

o = Solution()

# n3a = TreeNode(3)
# n4a = TreeNode(4)
# n5a = TreeNode(5)
# n1a = TreeNode(1)
# n2a = TreeNode(2)
# n0a = TreeNode(0)
#
# n3a.left = n4a
# n3a.right = n5a
# n4a.left = n1a
# n4a.right = n2a
# n2a.left = n0a
#
# n4b = TreeNode(4)
# n1b = TreeNode(1)
# n2b = TreeNode(2)
#
# n4b.left = n1b
# n4b.right = n2b
#
# print(o.isSubtree(n3a, n4b))

# n11= TreeNode(1)
# n12= TreeNode(1)
# n13= TreeNode(1)
# n14= TreeNode(1)
# n15= TreeNode(1)
# n16= TreeNode(1)
# n17= TreeNode(1)
# n18= TreeNode(1)
# n19= TreeNode(1)
# n20= TreeNode(1)
# n21= TreeNode(1)
# n22= TreeNode(2)
#
# n11.right = n12
# n12.right = n13
# n13.right = n14
# n14.right = n15
# n15.right = n16
# n16.right = n17
# n17.right = n18
# n18.right = n19
# n19.right = n20
# n20.right = n21
# n21.right = n22
#
#
#
# n31= TreeNode(1)
# n32= TreeNode(1)
# n33= TreeNode(1)
# n34= TreeNode(1)
# n35= TreeNode(1)
# n36= TreeNode(1)
# n37= TreeNode(2)
#
# n31.right = n32
# n32.right = n33
# n33.right = n34
# n34.right = n35
# n35.right = n36
# n36.right = n37


# n11= TreeNode(1)
# n12= TreeNode(1)
# n13= TreeNode(1)
# n14= TreeNode(1)
# n15= TreeNode(2)
#
# n21= TreeNode(1)
# n22= TreeNode(1)
# n23= TreeNode(2)
#
# n11.right = n12
# n12.right = n13
# n13.right= n14
# n14.right= n15
#
# n21.right = n22
# n22.right = n23

# print(o.isSubtree(n11, n21))

na = TreeNode(1)
nb = TreeNode(1)

na.right = nb

oa = TreeNode(1)

print(o.isSubtree(na,oa))


















