class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        res = []
        diff = float('inf')
        closest = 0
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp == target:
                    return target
                elif tmp < target:
                    j += 1
                else:
                    k -=1
                if abs(tmp - target) < diff:
                    diff = abs(tmp - target)
                    closest = tmp
        return closest
