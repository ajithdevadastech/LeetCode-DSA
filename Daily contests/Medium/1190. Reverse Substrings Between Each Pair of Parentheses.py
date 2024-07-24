class Solution(object):
    class Solution(object):
        def reverseParentheses(self, s):
            """
            :type s: str
            :rtype: str
            """
            stack = []
            k = 0
            for i in s:
                if i != '(':
                    #add to stack
                    stack.append(i)
                elif k > 0:
                    index = s.find(')')
                    st = self.reverseParentheses(s[k,index+1])

