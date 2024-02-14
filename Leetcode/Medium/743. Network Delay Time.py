import math
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """



        self.adj = []
        self.dist = [math.inf] * n
        self.dist[k-1] = 0
        self.pq = [(0,k-1)]

        for i in range(n):
            self.adj.append([])

        #populate self.adj

        for i in times:
            self.adj[i[0]-1].append([i[1]-1, i[2]])

        def computeDistance(node):
            while self.pq:
                calculateddist, currnode = heapq.heappop(self.pq)
                if self.dist[currnode] >= calculateddist:
                    for n, d in self.adj[currnode]:
                        if self.dist[n] > calculateddist + d:
                            self.dist[n] = calculateddist + d
                            heapq.heappush(self.pq, (self.dist[n], n))


        computeDistance(k-1)
        if max(self.dist) == math.inf:
            return -1
        else:
            return max(self.dist)


o = Solution()

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

print(o.networkDelayTime(times, n, k))