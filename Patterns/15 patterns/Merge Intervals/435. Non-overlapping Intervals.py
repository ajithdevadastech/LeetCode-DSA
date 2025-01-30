class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        '''
        sort the list
        popleft first element and add in stack
        compare first element in intervals with last element in stack.
        if stack[-1][1] <= fe[0], add fe to stack (no deletion)
        else 
            if fe[1] >= stack[-1][1], don't add, increment counter, move on to next element in intervals
            else pop from stack, insert fe into stack. move on with next element in intervals. increment counter.
        end when len(intervals) == 0
    
        '''

        if len(intervals) == 0 or len(intervals) == 1:
            return 0

        intervals.sort()

        k = intervals.pop(0)
        stack = [k]
        r = 0
        while len(intervals) > 0:
            f = intervals.pop(0)
            s = stack[-1]
            if s[1] <= f[0]:
                stack.append(f)
            else:
                if f[1] >= s[1]:
                    r = r + 1
                else:
                    stack.pop()
                    stack.append(f)
                    r = r + 1

        return r

o = Solution()
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(o.eraseOverlapIntervals(intervals))
