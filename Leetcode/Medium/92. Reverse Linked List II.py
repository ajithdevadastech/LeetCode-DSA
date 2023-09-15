# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverseList(self, head, right, i):

        if head.val is None:
            return head

        if head.next is None:
            return head


        k = head.next.next
        x = head.next
        curr = head
        temp = head
        #curr.next = None

        if k is None or i == right - 2:
            temp.next = x.next
            x.next = curr
            return x

        while True:
            if k is None or i == right - 2:
                temp.next = x.next
                x.next = curr
                return x
            else:
                tmp = x.next
                k = tmp.next
                x.next = curr
                curr = x
                i = i + 1
                x = tmp


    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head.next is None:
            return head

        r = head

        i = 1
        while True:
            if i == left-1:
                head.next = self.reverseList(head.next, right, i)
                break
            else:
                head = head.next
        return r

o = Solution()
# head = ListNode()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
left = 2
right = 4
print(o.reverseBetween(head, left, right))