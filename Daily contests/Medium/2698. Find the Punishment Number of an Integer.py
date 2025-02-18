import math
class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.flag = False
        self.sq = 0



        def helper(num, val):
            if num == 0:
                if val * val == self.sq:
                    self.flag = True
                return
            j = 1
            s = str(num)
            while j <= len(s):
                x = int(s[0:j])
                if j < len(s):
                    helper(int(s[j:]), val+x)
                else:
                    helper(0,val+x)
                j = j+1

        r = 0

        if n < 4:
            return 1
        else:
            r = 1

        for i in range(5,n+1):
            self.sq = i * i
            helper(self.sq, 0)
            if self.flag:
                r = r + i*i
                self.flag = False
        return r



o = Solution()
print(o.punishmentNumber(45))
