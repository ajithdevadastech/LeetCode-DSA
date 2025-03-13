class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        """
        1. find int(sqrt right) + 1
        2. create array of size right + 1
        3. apply sieve of eratosthenis on the array
        4. navigate from left to right indices in the array and find the minimum distant pair
        
        """

        sq_rt = int(right ** 0.5)

        arr = [1] * (right+1)
        arr[0] = 0
        arr[1] = 0


        for s in range(2,sq_rt+1):
            if arr[s] == 1:
                k = 2
                while k * s <= right:
                    arr[k * s] = 0
                    k = k + 1

        prev = None
        flag = False
        minpair = []
        mindist = float('Inf')
        i = left
        while i <= right:
            if arr[i] == 1:
                if prev is not None:
                    flag = True
                    if i - prev < mindist:
                        mindist = i - prev
                        minpair = [prev, i]
                prev = i
            i = i + 1
        if flag:
            return minpair
        else:
            return [-1,-1]


o = Solution()
left = 2000
right = 2100
print(o.closestPrimes(left, right))







