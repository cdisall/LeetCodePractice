class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp < 0:
                    j += 1
                elif tmp > 0:
                    k -=1
                else:
                    res.append(([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                    while nums[j]==nums[j-1] and j<k:
                        j += 1
                    while nums[k]==nums[k+1] and j<k:
                        k -= 1
        return res
