class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        """
        Algorithm
        -----------------
    
        a. if both numbers are greater than 0, then +1, return  sum() * 1
        b. if both numbers are less than zero, then -1, return sum() * -1
        c. if either of the number is less than 0, return difference * sign of max(abs(a),abs(b))
        
        sum()
        -----
        1. xor (a ^ b) the numbers for the sum without carry ons; x = sum
        2. find carry on (a & b) << 1; y = carryon. if y > 0, xor to x. x = sum, y = carry on. if y == 0, return x
        3. repeat step 2 with a & b substituted with x and y.
        
        
        difference()
        ------------
        1. xor (a^b) the numbers for the diff without carry ons; x = diff
        2. find borrow (~a & b) << 1; y = borrow. if y > 0, add to x. x = sum, y = carry on. if y == 0, return x.
        3. repeat step 2 with a & b substituted with x and y.
        
        """

        if a == 0:
            return b
        if b == 0:
            return a

        def findSum(x,y):
            s = x ^ y
            c = (x & y) << 1
            k = c
            while k > 0:
                j = s ^ c
                k = (s & c) << 1
                s = j
                c = k
            return s



        def findDiff(x,y):
            d = x ^ y
            c = (~x & y) << 1
            k = c
            while k > 0:
                j = d ^ c
                k = (~d & c) << 1
                d = j
                c = k
            return d




        if a > 0 and b > 0:
            return findSum(abs(a), abs(b)) * 1
        if a < 0 and b < 0:
            return findSum(abs(a), abs(b)) * -1
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            if abs(a) > abs(b):
                mul = 1
                if a < 0:
                    mul = -1
                return findDiff(abs(a), abs(b)) * mul
            elif abs(b) > abs(a):
                mul = 1
                if b < 0:
                    mul = -1
                return findDiff(abs(b), abs(a)) * mul
            else:
                return 0

o = Solution()
a = 5
b = 21
print(o.getSum(a,b))




