class Solution:
    def removeElement(self, nums, val):
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        return i