class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = [0] * n
        m[0] = nums[0]
        mx = m[0]
        for i in range(1, n):
            if m[i-1] > 0:
                m[i] = nums[i] + m[i-1]
            else:
                m[i] = nums[i]
            mx = max(m[i], mx)
        return mx
    