
from collections import Counter
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """

        if len(tasks) == 1:
            return -1

        d = Counter(tasks)

        r = 0
        for k in d.keys():
            if d[k] == 1:
                return -1
            if d[k] % 3 == 0:
                r = r + int(d[k]/3)
            else:
                r = r + int(d[k]/3) + 1
        return r




o = Solution()
tasks = [2,2,3,3,2,4,4,4,4,4]
print(o.minimumRounds(tasks))




