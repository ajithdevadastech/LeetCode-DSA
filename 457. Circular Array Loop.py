class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return True

        sp = 0
        fp = 0

        prev_fp = None

        while sp < len(nums):
            sp = (sp + nums[sp]) % len(nums)
            fp = (fp + nums[fp]) % len(nums)
            fp = (fp + nums[fp]) % len(nums)
            if sp == fp and prev_fp and fp != prev_fp:
                return True
            else:
                sp = sp + 1
            prev_fp = fp
        return False

o =  Solution()
nums = [1,-1,5,1,4]
print(o.circularArrayLoop(nums))