class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        """
        1. populate dict, reverse traversal, if exists, store value in array
        2. create result array with 0s
        3. use stack for next greater element.
        3. for each new element, see how far it goes and store the result array using the index poped from dict val
        
        """

        #1. populate dict, reverse traversal, if exists, store value in array

        # dict = {}
        # i = 0
        # while i <= len(temperatures) - 1:
        #     if temperatures[i] in dict.keys():
        #         dict[temperatures[i]].append(i)
        #     else:
        #         dict[temperatures[i]] = [i]
        #     i = i + 1

        #2. create result array with 0s

        r = [0]*len(temperatures)

        #stack operation for next greater element - modified

        stack = [[temperatures[0],0, 0]]
        i = 1
        while i < len(temperatures):
            if len(stack) == 0:
                stack.append([temperatures[i],0, i])
            elif stack[-1][0] >= temperatures[i]:
                stack.append([temperatures[i],0, i])
            else:
                k = 1
                while True:
                    if len(stack) == 0:
                        stack.append([temperatures[i],0,i])
                        break
                    elif stack[-1][0] >= temperatures[i]:
                        stack.append([temperatures[i],0,i])
                        break
                    else:
                        #ind = dict[stack[-1][0]].pop()
                        ind = stack[-1][2]
                        r[ind]= i - stack[-1][2]
                        stack.pop()
                        if len(stack) > 0:
                            stack[-1][1] = stack[-1][1] + k
                        k = k + 1
            i = i + 1

        return r

o = Solution()
temperatures = [64,40,49,73,72,35,68,83,35,73,84,88,96,43,74,63,41,95,48,46,89,72,34,85,72,59,87,49,30,32,47,34,74,58,31,75,73,88,64,92,83,64,100,99,81,41,48,83,96,92,82,32,35,68,68,92,73,92,52,33,44,38,47,88,71,50,57,95,33,65,94,44,47,79,41,74,50,67,97,31,68,50,37,70,77,55,48,30,77,100,31,100,69,60,47,95,68,47,33,64]
print(o.dailyTemperatures(temperatures))








