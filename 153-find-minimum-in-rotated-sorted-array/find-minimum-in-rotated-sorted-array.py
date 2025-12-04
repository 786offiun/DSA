class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums) - 1

        # If array is not rotated at all
        if nums[low] <= nums[high]:
            return nums[0]

        while low <= high:
            mid = (low + high) // 2

            # Check if mid is pivot (minimum element)
            # Case 1: mid < high and next element is smaller -> mid+1 is pivot
            if mid < high and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            # Case 2: mid > low and mid element is smaller than previous -> mid is pivot
            if mid > low and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Decide which half to search: if right part sorted, go left; else go right
            if nums[high] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return 0  # fallback if no rotation
        