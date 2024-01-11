class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        """
        1. if any of the symbol, pop twice from stack, calculate and append the result to stack
        2. else, just append to stack
        3. pop the result from the stack and return
        """

        if len(tokens) == 1:
            return int(tokens[0])

        symbols = ['+', '-', '*', '/']

        stack = []

        for t in tokens:
            if t not in symbols:
                stack.append(t)
            else:
                v2 = int(stack.pop())
                v1 = int(stack.pop())

                if t == '+':
                    stack.append(v1 + v2)
                elif t == '-':
                    stack.append(v1 - v2)
                elif t == '*':
                    stack.append(v1 * v2)
                else:
                    stack.append(int(v1 / v2))

        return stack.pop()


o = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(o.evalRPN(tokens))