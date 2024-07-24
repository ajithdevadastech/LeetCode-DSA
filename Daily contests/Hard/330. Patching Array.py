class Solution(object):
    def minpatches(self, nums, n):

        #expand nums and add in dict. p = 0
        #start from 1 to n and check for missing numbers in the key. return p
        # if missing
        ## add missing to dict, p += 1
        ## add missing to all dict keys and add them to dict keys if not there.

        dictChange = {}

        def helper(j,s):
            if s not in dictChange.keys():
                dictChange[s] = 1
            if j > len(nums) - 1:
                return
            

        i = 0
        for num in nums:
            helper(i,num)
            i+=1

        return dictChange.keys()


o = Solution()
nums = [1,2,3,4]
print(o.minpatches(nums, 10))





