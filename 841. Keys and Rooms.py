class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        dictRooms = {}
        dictRooms[0] = 1

        total = []
        total.append(0)

        max= []
        max.append(0)

        def helper(arr, r):
            for i in arr:
                if i not in dictRooms.keys():
                    if i > max[0]:
                        max[0] = i
                    if i == r:
                        return False
                    dictRooms[i] = 1
                    total[0] = total[0] + i
                    helper(rooms[i], i)

        r = 0
        for j in rooms:
            helper(j, r)
            r = r + 1

        if total[0] != (max[0] * (max[0] + 1)) / 2:
            return False
        else:
            return True

o = Solution()
rooms = [[2],[],[1]]
print(o.canVisitAllRooms(rooms))
