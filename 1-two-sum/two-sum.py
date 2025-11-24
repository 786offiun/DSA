class Solution(object):
    def twoSum(self, nums, target):
        ori = nums[:]


        left  = 0
        right = len(nums) - 1
        result = []
        nums.sort()

        for i in range(len(nums)) :
        
            s = nums[left] + nums[right]
            print(s,left , right , i)
            if s == target:

                result.append(nums[left])
                result.append(nums[right])
                break
            elif s > target:
                right -= 1
            else:
                left += 1

        # find ORIGINAL indices (correct even for duplicates)
        first_val = result[0]
        second_val = result[1]
        
        f = ori.index(first_val)
        ori[f] = None   # so second index is not same
        s = ori.index(second_val)
        return [f,s]
