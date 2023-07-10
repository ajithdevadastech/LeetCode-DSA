# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head.next:
            return -1

        sp = head
        fp = head

        # finding the intersection
        while True:
            sp = sp.next
            fp = fp.next.next
            if not fp:
                return -1
            if sp == fp:
                break

        # finding the meeting point
        sp = head
        s = 0
        while True:
            if sp == fp:
                return s
            else:
                s = s + 1
                sp = sp.next
                fp = fp.next


o = Solution()
nums = [1,2]
head = ListNode(nums[0])
root = head
pos = 0
ind = 0
for i in nums[1:]:
    root.next = ListNode(i)
    if pos == ind:
        j = root
    root = root.next
    ind = ind+1

root.next = j

print(o.detectCycle(head))










