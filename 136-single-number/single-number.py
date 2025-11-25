class Solution(object):
    def singleNumber(self, nums):
        u=0
        for i in range(len(nums)):
            u=u^nums[i]
        return u
        