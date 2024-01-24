class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        
        if n = 1, return 1
        1. populate 1 to n in stack1 with n at the bottom and 1 at top
        2. i = 0
        3. if i == 0, ignore every other element starting from first. move valid elements to stack2. set i = 1. return if len(stack2) = 1 with stack2[0]
        4. if i == 1, ignore every other element starting from first. move valid elements to stack1. set i = 0. return if len(stack1) = 1 with stack1[0]
     
        
        """

        stack1 = []
        stack2 = []

        if n == 1:
            return 1

        i = n
        while i > 0:
            stack1.append(i)
            i = i - 1

        i = 0
        while True:
            if i == 0:
                fi = 0
                while fi < n:
                    k = stack1.pop()
                    if fi % 2 != 0:
                        stack2.append(k)
                    fi = fi + 1
                    if len(stack1) == 0:
                        break
                if len(stack2) == 1:
                    return stack2[0]
                i = 1
            else:
                si = 0
                while si < n:
                    k = stack2.pop()
                    if si % 2 != 0:
                        stack1.append(k)
                    si = si + 1
                    if len(stack2) == 0:
                        break
                if len(stack1) == 1:
                    return stack1[0]
                i = 0

o = Solution()
n = 9
print(o.lastRemaining(n))
