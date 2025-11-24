class Solution(object):
    def twoSum(self, nums, target):
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort()  # sorts by value

        left = 0
        right = len(arr) - 1

        while left < right:
            s = arr[left][0] + arr[right][0]

            if s == target:
                return [arr[left][1], arr[right][1]]

            if s < target:
                left += 1
            else:
                right -= 1
