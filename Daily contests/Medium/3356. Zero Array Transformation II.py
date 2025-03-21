class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int

        https://www.youtube.com/watch?v=Ap8NIgIqM2A

        """
        flag = True
        for n in nums:
            if n != 0:
                flag = False
        if flag:
            return 0

        total = 0
        ind = 0

        diffArr = [0] * (len(nums) + 1)

        k = 0
        for query in queries:

            if ind > len(nums) - 1:
                return k
            k = k + 1
            #operation in diffArr
            if query[1] >= ind:
                diffArr[max(ind,query[0])] = diffArr[max(ind,query[0])] + query[2]
                diffArr[query[1]+1] = diffArr[query[1]+1] - query[2]

                while total + diffArr[ind] >= nums[ind]:
                    total = total + diffArr[ind]
                    ind = ind + 1
                    if ind > len(nums) - 1:
                        return k

        return -1



o = Solution()
nums = [7,6,8]
queries = [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]
print(o.minZeroArray(nums, queries))






