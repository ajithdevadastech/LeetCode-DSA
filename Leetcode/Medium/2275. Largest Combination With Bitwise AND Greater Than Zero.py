class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """

        self.flag = False
        self.r = 0

        if len(candidates) == 1:
            if candidates[0] == 0:
                return 0
            else:
                return 1

        def helper(val,index):
            if self.flag:
                return
            else:
                self.r = self.r + 1
                index = index + 1
                while index < len(candidates):
                    if self.flag:
                        return
                    else:
                        if val & candidates[index] > 0:
                            self.flag = True
                            return
                        else:
                            helper(val & candidates(index), index)



        helper(candidates[0],0)
        if self.flag:
            return self.r
        else:
            return 0


o = Solution()
candidates = [16,17,71,62,12,24,14]
print(o.largestCombination(candidates))