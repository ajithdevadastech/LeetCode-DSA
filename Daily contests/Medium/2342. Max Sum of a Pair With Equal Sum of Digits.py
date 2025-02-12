import heapq
class Solution(object):
    def maximumSum(self, nums):

        def sumOfDigits(num):
            s = 0
            while True:
                q = int(num/10)
                r = num % 10
                s = s + r
                num = q
                if num == 0:
                    return s

        flag = False
        dict = {}

        #populating dict with index = sum of digits and value = indices.
        for n in nums:
            sd = sumOfDigits(n)
            if sd in dict.keys():
                flag = True
                heapq.heappush(dict[sd],-n)
            else:
                dict[sd] = [-n]

        if flag is False:
            return -1

        #finding the maxval

        maxval = 0
        for k in dict.keys():
            if len(dict[k]) > 1:
                v1 = -1 * heapq.heappop(dict[k])
                v2 = -1 * heapq.heappop(dict[k])
                if v1 + v2 > maxval:
                    maxval =  v1 + v2

        return maxval



o = Solution()
nums = [10,12,19,14]
print(o.maximumSum(nums))

