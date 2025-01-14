class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        p1 = 0
        p2 = len(numbers) - 1

        while True:
            if numbers[p1] + numbers[p2] > target:
                p2 = p2-1
            elif numbers[p1] + numbers[p2] < target:
                p1 = p1 + 1
            else:
                return [p1+1,p2+1]
            if p1 == p2:
                break

o = Solution()
numbers = [2,7,11,15]
target = 9
print(o.twoSum(numbers,target))