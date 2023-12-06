"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1


"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        mul = 1
        if x < 0:
            mul = -1


        x = abs(x)

        rNum = 0

        while x > 0:
            temp = rNum * 10 + x % 10
            if (temp - (x % 10))/10 == rNum:
                rNum = temp
            elif temp >= 2 ** 31:
                return 0
            else:
                return 0
            x = x // 10

        return rNum * mul

o = Solution()
x = -654665
print(o.reverse(x))
