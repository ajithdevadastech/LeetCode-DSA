# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head.val is None:
            return head

        if head.next is None:
            return head


        k = head.next.next
        x = head.next
        curr = head
        curr.next = None

        if k is None:
            x.next = curr
            return x

        while True:
            if k is None:
                x.next = curr
                return x
            else:
                tmp = x.next
                k = tmp.next
                x.next = curr
                curr = x
                x = tmp


o = Solution()
# head = ListNode()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(o.reverseList(head).val)