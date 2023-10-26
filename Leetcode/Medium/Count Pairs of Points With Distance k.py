class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """

        dictCords = {}
        r = 0

        #expand first node and add them on dictCords

        firstNode = coordinates[0]
        i = 0
        while i <= k:
            x = firstNode[0] ^ i
            y = firstNode[1] ^ (k-i)
            dictCords[(x,y)] = [firstNode]
            i = i + 1

        r = 0
        i = 1

        while i < len(coordinates):
            linkNodes = []
            node = coordinates[i]
            if (node[0], node[1]) in dictCords.keys():
                r = r + len(dictCords[(node[0], node[1])])
                linkNodes = dictCords[(node[0], node[1])]
            #expand node
            j = 0
            while j <= k:
                x = node[0] ^ j
                y = node[1] ^ (k - j)
                if len(linkNodes) == 0:
                    dictCords[(x, y)] = [node]
                else:
                    if (x,y) in dictCords.keys():
                        dictCords[(x,y)].append(node)
                    else:
                        dictCords[(x, y)] = [node]
                j = j + 1
            i = i + 1
        return r

o = Solution()
coordinates = [[1,2],[4,2],[1,3],[5,2]]
k = 5
print(o.countPairs(coordinates, k))