class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.answers = []
        #recursion function

        def frecur (index, combination, remVal):
            if remVal == 0:
                self.answers.append(combination)
                return
            else:
                index = index + 1
                if index > len(candidates) - 1:
                    return
                else:
                    m = index
                    while m < len(candidates):
                        candnumR = remVal // candidates[m]
                        l = 0
                        combR = combination
                        remR = remVal
                        while l < candnumR:
                            combR = combR + [candidates[m]]
                            remR = remR - candidates[m]
                            frecur(m, combR, remR)
                            l = l + 1
                        m = m + 1


        #driver code
        i = 0
        while i < len(candidates):
            candnum = target//candidates[i]
            j = 0
            combArr = []
            rem = target
            while j < candnum:
                combArr = combArr + [candidates[i]]
                rem = rem - candidates[i]
                frecur(i, combArr, rem)
                j = j + 1
            i = i + 1

        return self.answers

o = Solution()

# candidates = [2,3,6,7]
# target = 7

# candidates = [2,3,5]
# target = 8

# candidates = [3,5,8]
# target = 11

# candidates = [8,7,4,3]
# target = 11

candidates = [3,8,4,6]
target = 11

print(o.combinationSum(candidates, target))






