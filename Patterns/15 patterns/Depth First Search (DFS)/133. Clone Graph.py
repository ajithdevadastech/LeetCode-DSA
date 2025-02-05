class Node(object):
    def __init__(self, val = None, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):

    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node):

        if node is None:
            return node

        if node in self.visited.keys():
            return self.visited[node]

        #create new node

        c = Node(node.val)
        self.visited[node] = c

        #expand new node
        for n in node.neighbors:
            c.neighbors.append(self.cloneGraph(n))

        return node







o = Solution()
adjList = [[2,4],[1,3],[2,4],[1,3]]
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
print(o.cloneGraph(node1))


