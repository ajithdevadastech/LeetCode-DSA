class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """

        used = {}

        n = len(pattern)
        s = ''

        self.r = ''

        def helper(s, ind):
            if len(used) == len(pattern) + 1:
                self.r = s
                return self.r
            else:
                i = 1
                while i <= n+1:
                    if pattern[ind] == 'I':
                        if i not in used.keys():
                            if i > int(s[-1]):
                                used[i] = 1
                                if helper(s + str(i), ind+1):
                                    return s
                                else:
                                    del used[i]
                    else:
                        if i not in used.keys():
                            if i < int(s[-1]):
                                used[i] = 1
                                if helper(s + str(i), ind+1):
                                    return s
                                else:
                                    del used[i]
                    i = i + 1
                if i > n+1:
                    return

        for i in range(1, n+2):
            s=str(i)
            used[i] = 1
            if helper(s,0):
                return self.r
            else:
                s = ''
                used = {}

o = Solution()
pattern = "DDD"
print(o.smallestNumber(pattern))





