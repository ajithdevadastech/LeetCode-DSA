# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    rHead = None
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            return head

        curr = head
        next = curr.next
        curr.next = None

        while next.next:
            k = next.next
            next.next = curr
            curr = next
            next = k
        next.next = curr
        return next

k = ListNode(1)
k.next = ListNode(2)
k.next.next = ListNode(3)
k.next.next.next = ListNode(4)
k.next.next.next.next = ListNode(5)

o=Solution()
print(o.reverseList(k).val)
