class Solution(object):
    def orangesRotting(self, grid):

        visited = {}

        deque = []

        r = len(grid)
        c = len(grid[0])

        gridval = [[0] * c for i in range(r)]


        maxval = 0

        i = 0
        while i < r:
            j = 0
            while j < c:
                if (i,j) not in visited.keys():
                    queue = []
                    if grid[i][j] == 2:
                        #check all directions and add in queue, pop from queue, repeat until queue is empty
                        queue.append([0, [i,j]])
                        while len(queue) > 0:
                            k = queue.pop(0)
                            #add neighbors from all sides
                            dist = k[0]
                            x = k[1][0]
                            y = k[1][1]
                            visited[(x, y)] = 1
                            if gridval[x][y] == 0:
                                if dist > 0:
                                    gridval[x][y] = dist
                            else:
                                gridval[x][y] = min(dist,gridval[x][y])

                            if x-1 >= 0 and grid[x-1][y] == 1:
                                if (x-1,y) not in visited.keys():
                                    #grid[x - 1][y] = 2
                                    queue.append([dist+1,[x-1,y]])
                                else:
                                    if dist+1 < gridval[x-1][y]:
                                        queue.append([dist + 1, [x - 1, y]])

                            if x+1 < r and grid[x+1][y] == 1:
                                if (x+1,y) not in visited.keys():
                                    #grid[x+1][y] = 2
                                    queue.append([dist + 1, [x + 1, y]])
                                else:
                                    if dist+1 < gridval[x+1][y]:
                                        queue.append([dist + 1, [x+1, y]])
                            if y-1 >= 0 and grid[x][y-1] == 1:
                                if (x,y-1) not in visited.keys():
                                    #grid[x][y-1] = 2
                                    queue.append([dist + 1, [x, y-1]])
                                else:
                                    if dist+1 < gridval[x][y-1]:
                                        queue.append([dist + 1, [x, y-1]])
                            if y+1 < c and grid[x][y+1] == 1:
                                if (x, y + 1) not in visited.keys():
                                    #grid[x][y+1] = 2
                                    queue.append([dist + 1, [x, y+1]])
                                else:
                                    if dist+1 < gridval[x][y+1]:
                                        queue.append([dist + 1, [x, y+1]])

                j = j + 1
            i = i + 1

        i = 0
        while i < r:
            j = 0
            while j < c:
                if grid[i][j] == 1 and (i,j) not in visited.keys():
                    return -1
                if gridval[i][j] > maxval:
                    maxval = gridval[i][j]
                j = j + 1
            i = i + 1

        return maxval



o = Solution()
grid = [[2,1,1],[1,1,1],[0,1,2]]
print(o.orangesRotting(grid))













