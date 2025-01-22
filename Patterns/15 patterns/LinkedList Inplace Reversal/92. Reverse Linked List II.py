# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        if head is None:
            return head

        if head.next is None:
            return head

        #takes current node, right value, reverses list, returns right node
        def reverseHelper(nHead, left, right):
            curr = nHead
            next = curr.next
            l = None
            i = left+1
            if next.next is None:
                next.next = curr
            else:
                while True:
                    if i >= right:
                        l = next.next
                        next.next = curr
                        break
                    k = next.next
                    next.next = curr
                    curr = next
                    next = k
                    i = i + 1

            return next, l

        #reach until left and store left
        if left == right:
            return head
        left = left - 1
        right = right - 1
        prev = None
        curr = head
        i = 0
        while i != left:
            prev = curr
            curr = curr.next
            i = i + 1

        j = prev
        k, l = reverseHelper(curr, left, right)
        curr.next = l
        if j is None:
            head = k
        else:
            j.next = k
        return head


k = ListNode(1)
k.next = ListNode(2)
k.next.next = ListNode(3)
k.next.next.next = ListNode(4)
k.next.next.next.next = ListNode(5)
k.next.next.next.next.next = ListNode(6)


o = Solution()
print(o.reverseBetween(k, 2,6))


