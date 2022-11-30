# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False

        if head.next is None:
            return True

        if head.next.next is None:
            if head.val != head.next.val:
                return False
            else:
                return True

        if head.next.next.next is None:
            if head.val != head.next.next.val:
                return False
            else:
                return True

        #find the middle node

        slow = head
        fast = head.next
        middle = None

        while True:
            if fast is None:
                middle = slow
                break
            if fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            else:
                middle = slow
                break

        #reverse from middle to end


        prev = middle.next
        temp1 = prev
        head1 = prev.next
        finalNode = None
        temp1.next = None
        while True:
            if head1 is None:
                finalNode = prev
                middle.next = finalNode
                break
            temp = head1
            head1 = head1.next
            temp.next = prev
            prev = temp


       # start from first and middle. Compare

        lf = head
        rf = middle.next

        while True:
            if rf is None:
                break
            if lf.val != rf.val:
                return False
            lf = lf.next
            rf = rf.next

        return True


o = Solution()

# head = ListNode (1)
# head.next = ListNode (2)
# head.next.next = ListNode (2)
# head.next.next.next = ListNode (1)

# head = ListNode (1)
# head.next = ListNode (2)
# head.next.next = ListNode (1)
# head.next.next.next = ListNode (2)
# head.next.next.next.next = ListNode (1)

# head = ListNode (1)
# head.next = ListNode (2)

head = ListNode (1)
head.next = ListNode (3)
head.next.next = ListNode (2)
head.next.next.next = ListNode (4)
head.next.next.next.next = ListNode (2)
head.next.next.next.next.next = ListNode (3)
head.next.next.next.next.next.next = ListNode (1)

print(o.isPalindrome(head))
