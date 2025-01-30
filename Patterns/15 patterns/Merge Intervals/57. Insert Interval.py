class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        """
        continue pop and populate stack for all elements where  ni[1] < i[0]
 
        if ni[1] >= i[0] and ni[1] <= i[1], right element = i[1], navigate ni[0] until it reaches an i[0] >= ni[0], left element = i[0]
        if ni[1] > i[1], right element = ni[1], navigate ni[0] until it reaches an i[0] <= ni[0], left element = i[0]
        if ni[0] is outside of an interval while traversing, need all items below it and left element is ni[0]
        if ni[0] is on boundaries or within the interval, need all intervals below it and left element is i[0] of that interval
        populate back the items from stack.
        
        """

        if len(intervals) == 0:
            return [newInterval]

        r = []

        #continue pop and populate stack for all elements where  ni[1] < i[0]

        stack = []
        i = len(intervals) - 1
        while True:
            if intervals[i][0] > newInterval[1]:
                k = intervals.pop()
                stack.append(k)
            else:
                break
            if len(intervals) == 0:
                r.append(newInterval)
                while len(stack) > 0:
                    k = stack.pop()
                    r.append(k)
                return r
            i = i - 1

        re = None
        if newInterval[1] >= intervals[-1][0] and newInterval[1] <= intervals[-1][1]:
            re = intervals[-1][1]

        if newInterval[1] > intervals[-1][1]:
            re = newInterval[1]


        le = None
        i = len(intervals) - 1
        while True:
            if newInterval[0] > intervals[i][1]:
                le = newInterval[0]
                j = 0
                while j <= i:
                    r.append(intervals[j])
                    j = j + 1
                r.append([le,re])
                break
            elif newInterval[0] <= intervals[i][1] and newInterval[0] >= intervals[i][0]:
                le = intervals[i][0]
                j = 0
                while j <= i-1:
                    r.append(intervals[j])
                    j = j + 1
                r.append([le, re])
                break
            i = i - 1
            if i < 0:
                r.append([newInterval[0],re])
                break

        #add back from stack

        while len(stack) > 0:
            k = stack.pop()
            r.append(k)

        return r

o = Solution()
intervals = [[2,5],[6,7],[8,9]]
newInterval = [0,1]
print(o.insert(intervals, newInterval))



