class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mx = 0
        mn = nums[0]
        for i in range(1, len(nums)):
            mx = max(nums[i] - mn, mx)
            mn = min(nums[i], mn)
        if mx == 0:
            return -1
        return mx