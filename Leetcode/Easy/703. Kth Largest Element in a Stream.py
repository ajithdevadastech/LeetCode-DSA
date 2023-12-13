import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.minheap = nums[0:k]
        self.k = k
        heapq.heapify(self.minheap)

        i = k
        while i < len(nums):
            heapq.heappush(self.minheap, nums[i])
            heapq.heappop(self.minheap)
            i = i + 1


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)
            heapq.heappop(self.minheap)

        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:

# obj = KthLargest(3, [4, 5, 8, 2])
# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))

obj = KthLargest(1, [])
print(obj.add(-3))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(0))
print(obj.add(4))
