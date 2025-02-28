
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.visitedB = False
        self.MinsB = None

class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """

        #create node dict

        edges.sort()

        self.nodedict = {}
        self.nodeF = {}
        self.nodeB = {}

        self.val = float('-Inf')

        for e in edges:
            if e[0] not in self.nodedict.keys():
                self.nodedict[e[0]] = Node(e[0])
            if e[1] not in self.nodedict.keys():
                self.nodedict[e[1]] = Node(e[1])

        for e in edges:
            if e[0] not in self.nodeF.keys():
                self.nodeF[e[0]] = [e[1]]
            else:
                self.nodeF[e[0]].append(e[1])

        for e in edges:
            if e[1] not in self.nodeB.keys():
                self.nodeB[e[1]] = [e[0]]
            else:
                self.nodeB[e[1]].append(e[0])

        i = 0
        for n in self.nodedict.values():
            n.val = amount[i]
            i = i + 1

        def traverseB(mins,pos):
            self.nodedict[pos].visitedB = True
            self.nodedict[pos].MinsB = mins
            if pos == 0:
                return True
            else:
                if traverseB(mins+1,self.nodeB[pos][0]):
                    return

        def traverseA(node, s, mins):
            if self.nodedict[node].visitedB:
                if mins == self.nodedict[node].MinsB:
                    s = s + int(self.nodedict[node].val/2)
                if mins < self.nodedict[node].MinsB:
                    s = s + self.nodedict[node].val
            else:
                s = s + self.nodedict[node].val

            if node not in self.nodeF.keys():
                if s > self.val:
                    self.val = s
                return
            else:
                for k in self.nodeF[node]:
                    traverseA(k,s,mins+1)


        traverseB(0, bob)

        #check all paths of A and fetch the greatest path

        traverseA(0, 0, 0)

        return self.val



o = Solution()
# edges = [[0,1],[1,2],[1,3],[3,4]]
# bob = 3
# amount = [-2,4,2,-4,6]
# edges = [[0,1]]
# bob = 1
# amount = [-7280,2350]
edges = [[0,2],[0,4],[1,3],[1,2]]
bob = 1
amount = [3958,-9854,-8334,-9388,3410]
print(o.mostProfitablePath(edges,bob,amount))



































