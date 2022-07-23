class Solution:
    def findMin(self, nums):
        # Find rotation
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[(j)] < nums[(mid)]:
                i = mid + 1
            else:
                j = mid
        return nums[i]