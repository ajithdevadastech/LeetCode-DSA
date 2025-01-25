class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):

        if head is None or head.next is None:
            return head

        #find p1,c1,n1

        i = 1
        curr = head
        prev = None
        while i < k:
            prev = curr
            curr = curr.next
            i = i + 1
        p1 = prev
        c1 = curr
        n1 = curr.next

        #find p2, c2, n2

        ptr1 = head
        ptr2 = curr
        j = 1
        prev = None
        while ptr2.next:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        p2 = prev
        c2 = ptr1
        n2 = c2.next

        if i > j:
            k1 = p1
            k2 = c1
            k3 = n1
            p1 = p2
            c1 = c2
            n1 = n2
            p2 = k1
            c2 = k2
            n2 = k3

        if c1 == c2:
            return head
        if c1.next == c2:
            if p1:
                p1.next = c2
            else:
                head = c2
            if c2: c2.next = c1
            if c1: c1.next = n2
        elif c1.next.next == c2:
            if p1:
                p1.next = c2
            else:
                head = c2
            if c2: c2.next = n1
            if n1: n1.next = c1
            if c1: c1.next = n2
        else:
            if p1:
                p1.next = c2
            else:
                head = c2
            if c2: k = c2.next
            if c2: c2.next = n1
            if p2: p2.next = c1
            if c1: c1.next = k

        return head


o = Solution()

arr = [7,9,6,6,7,8,3,0,9,5]


x = ListNode(arr[0])
head =  x
i = 1
while i < len(arr):
    x.next = ListNode(arr[i])
    x = x.next
    i = i + 1

k = 5
print(o.swapNodes(head, k))




