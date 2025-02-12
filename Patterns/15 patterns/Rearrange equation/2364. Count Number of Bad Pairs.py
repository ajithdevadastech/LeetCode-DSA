class Solution(object):
    def countBadPairs(self, nums):

        #hashmap
        hm = {}
        i = 0
        s = 0
        for n in nums:
            if i-n in hm.keys():
                hm[i-n] = hm[i-n] + 1
            else:
                hm[i-n] = 1
            s = s + i
            i = i + 1

        d = 0
        for v in hm.values():
            if v > 0:
                d = d + int(v * (v - 1)/2)

        return s - d

o = Solution()
nums = [1,2,3,4,5]
print(o.countBadPairs(nums))

