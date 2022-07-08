from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        # Break problem into the 2sum problem by fixing each pair
        for i in range(n-3):
            for j in range(i+1, n-2):
                two_sum = nums[i]+nums[j]
                l = j+1
                r = n-1
                # Use pointers to find 2sum equal to target - the fixed 2sum
                while l<r:
                    four_sum = two_sum + nums[l] + nums[r]
                    if four_sum == target:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l+=1
                        r-=1
                    elif four_sum < target:
                        l+=1
                    else:
                        r-=1
        return (set(res))

