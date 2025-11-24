class Solution(object):
    def singleNumber(self, nums):
        u=0
        for i in nums:
            u^=i
        return u 
        