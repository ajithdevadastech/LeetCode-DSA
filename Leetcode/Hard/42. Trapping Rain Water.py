class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxL = height[0]
        maxR = height[len(height) - 1]

        l = 0
        r = len(height) - 1

        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > maxL:
                    maxL = height[l]
                if maxL - height[l] > 0:
                    water = water + maxL - height[l]
                l = l + 1
            else:
                if height[r] > maxR:
                    maxR = height[r]
                if maxR - height[r] > 0:
                    water = water + maxR - height[r]
                r = r - 1

        return water
