class ProductOfNumbers(object):

    def __init__(self):
        self.arr = []
        self.zero = None


    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.arr) == 0:
            self.arr.append(num)
        else:
            if self.arr[-1] == 0:
                self.zero = len(self.arr) - 1
                self.arr.append(num)
            else:
                self.arr.append(num * self.arr[-1])


    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if self.zero is not None:
            if len(self.arr) - k <= self.zero:
                return 0
            else:
                if self.arr[len(self.arr) - k - 1] == 0:
                    return self.arr[-1]
                else:
                    if len(self.arr) - k - 1 < 0:
                        return self.arr[-1]
                    else:
                        return self.arr[-1]/self.arr[len(self.arr) - k - 1]
        else:
            if len(self.arr) - k - 1 < 0:
                return self.arr[-1]
            else:
                return self.arr[-1] / self.arr[len(self.arr) - k - 1]



p = ProductOfNumbers()
p.add(0)
p.add(5)
p.add(6)
print(p.getProduct(2))
print(p.getProduct(2))
p.add(8)
print(p.getProduct(4))
p.add(2)

# p.getProduct(4)
# p.add(8)
# p.getProduct(2)