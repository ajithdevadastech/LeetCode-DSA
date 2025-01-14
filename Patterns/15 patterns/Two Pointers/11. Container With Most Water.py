class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        def area (p1,p2):
            return (p2-p1) * min(height[p1], height[p2])

        p1 = 0
        p2 = len(height) - 1

        maxarea = area(p1,p2)

        while True:
            if height[p1] <= height[p2]:
                p1 = p1 + 1
            else:
                p2 = p2 - 1
            if p1 >= p2:
                break
            else:
                if area(p1,p2) > maxarea:
                    maxarea = area(p1,p2)
        return maxarea


o = Solution()
#height = [1,8,6,2,5,4,8,3,7]
height = [1,3,2,5,25,24,5]
print(o.maxArea(height))





