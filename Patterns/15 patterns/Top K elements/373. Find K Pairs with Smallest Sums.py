import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        visited = set()
        ans = []

        h = [(nums1[0] + nums2[0], (0,0))]
        visited.add((0,0))
        heapq.heapify(h)

        i = 0
        while i < k:
            #pop from heap
            p = heapq.heappop(h)
            ans.append([nums1[p[1][0]], nums2[p[1][1]]])
            index1 = p[1][0]
            index2 = p[1][1]

            #push neighboring nodes into heap

            #node1
            i1 = index1 + 1
            j1 = index2
            if i1 > len(nums1) - 1 and j1 > len(nums2) - 1:
                break
            if i1 <= len(nums1) - 1 and j1 <= len(nums2) - 1:
                if (i1,j1) not in visited:
                    visited.add((i1,j1))
                    heapq.heappush(h, (nums1[i1] + nums2[j1], (i1,j1)))

            #node2
            i1 = index1
            j1 = index2 + 1
            if i1 > len(nums1) - 1 and j1 > len(nums2) - 1:
                break
            if i1 <= len(nums1) - 1 and j1 <= len(nums2) - 1:
                if (i1,j1) not in visited:
                    visited.add((i1, j1))
                    heapq.heappush(h, (nums1[i1] + nums2[j1], (i1, j1)))

            i = i + 1
        return ans

o = Solution()

nums1 = [1,7,11]
nums2 = [2,4,20]
k = 8

print(o.kSmallestPairs(nums1, nums2, k))

