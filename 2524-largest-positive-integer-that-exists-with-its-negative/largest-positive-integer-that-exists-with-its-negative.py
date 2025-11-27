class Solution(object):
    def findMaxK(self, nums):
        nums.sort(reverse=True)
       
        for i in range(len(nums)):
             negval=(nums[i])*(-1)
            
             if negval in nums:
                 return nums[i]
        return -1


       
       
        