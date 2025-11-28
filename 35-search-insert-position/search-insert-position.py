class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        nums.sort()
        if nums[0]>=target:
            return 0
        if nums[len(nums)-1]<=target:
            return len(nums)

        for i in range(len(nums)-1):
            if target>= nums[i] and target<=nums[i+1]:
                return i+1
        

            
       
       