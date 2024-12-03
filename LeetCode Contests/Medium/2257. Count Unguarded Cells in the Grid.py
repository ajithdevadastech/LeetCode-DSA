class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """

        #initialize 2d array
        arr = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append('')
            arr.append(temp)

        #mark all guards

        for i in guards:
            arr[i[0]][i[1]] = 'G'

        #mark all walls

        for j in walls:
            arr[j[0]][j[1]] = 'W'

        #fill all guarded cells

        for k in guards:
            x = k[0]
            y = k[1]
            #search left
            l = y-1
            while l >= 0:
                if arr[x][l] != 'X':
                    if arr[x][l] != 'G' and arr[x][l] != 'W':
                        arr[x][l] = 'X'
                    else:
                        break
                l = l - 1
            #search right
            r = y + 1
            while r <= n-1:
                if arr[x][r] != 'X':
                    if arr[x][r] != 'G' and arr[x][r] != 'W':
                        arr[x][r] = 'X'
                    else:
                        break
                r = r + 1
            #search top
            t = x - 1
            while t >= 0:
                if arr[t][y] != 'X':
                    if arr[t][y] != 'G' and arr[t][y] != 'W':
                        arr[t][y] = 'X'
                    else:
                        break
                t = t - 1
            #search bottom:
            b = x + 1
            while b <= m-1:
                if arr[b][y] != 'X':
                    if arr[b][y] != 'G' and arr[b][y] != 'W':
                        arr[b][y] = 'X'
                    else:
                        break
                b = b + 1

        #count blank cells
        r = 0
        for x in range(m):
            for y in range(n):
                if arr[x][y] == '':
                    r = r + 1

        return r

o = Solution()
m = 4
n = 3
guards = [[1,0]]
walls = [[0,0],[1,2],[0,2],[2,1],[0,1],[2,2]]
print(o.countUnguarded(m,n,guards,walls))









