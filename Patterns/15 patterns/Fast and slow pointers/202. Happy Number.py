class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True

        def calculate(num):
            val = 0
            while True:
                val = val + (num%10)**2
                num = num//10
                if num == 0:
                    break
            return val


        slow = n
        fast = calculate(n)

        while True:
            if slow == fast:
                return False
            else:
                slow = calculate(slow)
                fast = calculate(calculate(fast))
                if fast == 1:
                    break
        return True

o = Solution()
n= 1
print(o.isHappy(n))