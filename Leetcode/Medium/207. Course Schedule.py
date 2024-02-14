class Solution(object):
    loop = False

    # initialize neighbors array, state array and flag

    neighbors = []
    state = []
    flag = False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        """
        1. initialize neighbors array, state array, flag
        2. set neighbors array for each course
        3. set state to 'U' for all courses
        4. loop through the courses and dfs through neighbors, if state = u. else, if flag = True, return False, else return true
        5. dfs - if state = U, mark state = V for all visited courses and mark P on all touched nodes. if state  = v for any node, mark flag = true

        """

        # 2. set neighbors array for each course, set state to U for all courses

        for nc in range(numCourses):
            self.neighbors.append([])
            self.state.append('U')

        for pr in prerequisites:
            self.neighbors[pr[1]].append(pr[0])

        def dfs(n):
            if self.state[n] == 'U':
                self.state[n] = 'V'
                for nei in self.neighbors[n]:
                    dfs(nei)
                self.state[n] = 'P'
            elif self.state[n] == 'V':
                self.flag = True

        for nc in range(numCourses):
            if self.state[nc] == 'U':
                dfs(nc)
            elif self.flag == True:
                self.neighbors = None
                self.state = None
                self.flag = None
                return False

        self.neighbors = None
        self.state = None
        self.flag = None
        return True

o = Solution()
numCourses = 4
prerequisites = [[1,0],[2,1],[0,2],[0,3]]

print(o.canFinish(numCourses, prerequisites))




