class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        L = len(nums)

        #move right
        ##################
        #take start s and distance d
        # return s + d%L


        #move left
        ################
        # take start s and distance d
        # return s + L - d%L


        def moveRight(s,d):
            return s + d%L

        def moveLeft (s,d):
            return s + L - d%L

        i = 0
        while i < L:
            slow = i
            fast = i
            while True:
                #move slow

                slowprev = slow
                if nums[slow] > 0:
                    slow = moveRight(slow, nums[slow])
                else:
                    slow = moveLeft(slow, nums[slow])

                #move fast

                fastprev = fast
                if nums[fast] > 0:
                    fast = moveRight(fast, nums[fast])
                    if nums[fast] > 0:
                        fast = moveRight(fast, nums[fast])
                    else:
                        fast = moveLeft(fast, nums[fast])
                else:
                    fast = moveLeft(fast, nums[fast])
                    if nums[fast] > 0:
                        fast = moveRight(fast, nums[fast])
                    else:
                        fast = moveLeft(fast, nums[fast])

                if slowprev == slow:
                    break
                elif (nums[slow] < 0 and nums[fast] > 0) or  (nums[slow] > 0 and nums[fast] < 0):
                    break
                elif slow == fast:
                    return True
            i+=1

        return False


o = Solution()
nums = [2,-1,1,2,2]
print(o.circularArrayLoop(nums))



