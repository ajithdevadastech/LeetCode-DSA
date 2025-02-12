import heapq


class NumberContainers(object):

    def __init__(self):
        self.dict = {}
        self.dict1 = {}

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        self.dict[index] = number

        if number not in self.dict1.keys():
            self.dict1[number] = index
            heapq.heapify(self.dict1[number])
        else:
            heapq.heappush(self.dict1[number],index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number in self.dict1.keys():
            while len(self.dict1[number]) > 0:
                k = heapq.heappop(self.dict1[number])
                if self.dict[k] == number:
                    return k
            return -1
        else:
            return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)