class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        """
        1. populate neighbors for all courses
        2. populate state for all courses
        3. if state = u, then dfs. Else, if flag = True, then return []
        4. dfs
        4.a. if state = u, set state = v, then dfs through neighbors.
        4.b. in the end set state = p and add to stack.
        4.c. if state = v, set flag = true
        
        """

        def dfs(n):
            if self.state[n] == 'U':
                self.state[n] = 'V'
                for nei in self.neighbors[n]:
                    dfs(nei)
                self.state[n] = 'P'
                self.stack.append(n)
            elif self.state[n] == 'V':
                self.flag = True

        self.neighbors = []
        self.state = []
        self.flag = False
        self.stack = []

        for i in range(numCourses):
            self.neighbors.append([])
            self.state.append('U')

        for pr in prerequisites:
            self.neighbors[pr[1]].append(pr[0])

        for j in range(numCourses):
            if self.state[j] == 'U':
                dfs(j)
            elif self.flag:
                return []

        r = []
        while len(self.stack) > 0:
            r.append(self.stack.pop())
        return r


o = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(o.findOrder(numCourses, prerequisites))





