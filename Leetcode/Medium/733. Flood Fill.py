class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        self.image = image
        self.value = image[sr][sc]
        self.visited = []


        m = len(image)
        n = len(image[0])

        for i in range(m):
            self.visited.append(['U'] * n)

        def dfs(r,c):
            self.image[r][c] = color
            self.visited[r][c] = 'V'

            if r-1 >= 0 and self.image[r-1][c] == self.value and self.visited[r-1][c] == 'U':
                dfs(r-1, c)
            if c-1 >= 0 and self.image[r][c-1] == self.value and self.visited[r][c-1]  == 'U':
                dfs(r, c-1)
            if c+1 <= n-1 and self.image[r][c+1] == self.value and self.visited[r][c+1] == 'U':
                dfs(r, c+1)
            if r+1 <= m-1 and self.image[r+1][c] == self.value and self.visited[r+1][c] == 'U':
                dfs(r+1, c)


        dfs(sr, sc)
        return self.image

o = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2


print(o.floodFill(image, sr, sc, color))

