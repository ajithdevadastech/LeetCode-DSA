
import math
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """

        self.memo = {}

        #populate tasks in has table

        self.tasks = {}
        for t in tasks:
            if t not in self.tasks.keys():
                self.tasks[t] = 1
            else:
                self.tasks[t] += 1

        def helper(count):
            if count == 1:
                return float('inf')
            elif count == 2 or count == 3:
                return 1
            else:
                if count in self.memo.keys():
                    return self.memo[count]
                else:
                    self.memo[count] = min(helper(count-2), helper(count-3)) + 1
                    return self.memo[count]

        r = 0
        for t in self.tasks.keys():
            k = helper(self.tasks[t])
            if k == float('inf'):
                return -1
            else:
                r = r + k

        return r

o = Solution()
tasks = [2,2,3,3,2,4,4,4,4,4]
print(o.minimumRounds(tasks))




