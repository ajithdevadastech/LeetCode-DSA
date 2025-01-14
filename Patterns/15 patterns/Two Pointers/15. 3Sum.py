class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort nums

        nums.sort()

        def twoSum(p1, p2, target):
            k = []
            while True:
                if nums[p1] + nums[p2] > target:
                    p2 = p2 - 1
                elif nums[p1] + nums[p2] < target:
                    p1 = p1 + 1
                else:
                    if [nums[p1],nums[p2]] not in k:
                        k.append([nums[p1],nums[p2]])
                    p1 = p1 + 1
                    p2 = p2 - 1
                if p1 >= p2:
                    break

            return k

        r = []
        i = 0
        prev = None
        for n in nums:
            if n != prev:
                p1 = i + 1
                p2 = len(nums) - 1
                target = -1 * n
                arr = twoSum(p1,p2,target)
                if len(arr) > 0:
                    j = 0
                    while j < len(arr):
                        r.append([n, arr[j][0], arr[j][1]])
                        j = j + 1
            i = i + 1
            if i == len(nums)-2:
                break
            prev = n

        return r

o = Solution()
#nums = [-1,0,1,2,-1,-4]
#nums = [-2,0,0,2,2]
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(o.threeSum(nums))


