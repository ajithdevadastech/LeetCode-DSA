import heapq


class MedianFinder(object):

    def __init__(self):

        self.maxheapmin = 0
        self.minheapmax = 0
        self.maxheap = []
        self.minheap = []
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        """
        algorithm
        -----------
        
        1. add to maxheap, then push to minheap
        2. if len(maxheap) < len(minheap), pop from minheap and push to maxheap
        """
        heapq.heappush(self.maxheap, -1 * num)
        heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))

        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))




    def findMedian(self):
        """
        :rtype: float
        """

        """
        algorithm
        -------------
        if maxheaplen == minheaplen == 0: avg max(maxheap) and min(minheap)
        else if maxheaplen > minheaplen, max(maxheap) else min(minheap)
        
        """

        if len(self.maxheap) == len(self.minheap):
            return (float)((-1 * self.maxheap[0]) + self.minheap[0])/2
        else:
            if len(self.maxheap) > len(self.minheap):
                return -1 * self.maxheap[0]
            else:
                return self.minheap[0]

o = MedianFinder()
o.addNum(1)
o.addNum(2)
print(o.findMedian())
o.addNum(3)
print(o.findMedian())



