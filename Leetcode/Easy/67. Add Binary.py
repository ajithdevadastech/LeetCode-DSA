class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        #logical and and 1 bit left shift

        x = int(a,2)
        y = int(b,2)

        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x = ans
            y = carry
        return bin(x)[2:]


o = Solution()
a = "1010"
b = "1011"
print(o.addBinary(a, b))