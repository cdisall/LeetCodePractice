from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Keep track of closest sum to target
        least_dist = target - (nums[0] + nums[1] + nums[2])
        # Iterate through nums
        for a in range(n - 2):
            # Create left and right pointers
            b = a + 1
            c = n - 1
            while b < c:
                # Get distance
                cur_dist = target - (nums[a] + nums[b] + nums[c])
                # Return current sum if equal to target
                if cur_dist == 0:
                    return target
                # Check if current distance is least
                if abs(cur_dist) < abs(least_dist):
                    least_dist = cur_dist

                # Increment left pointer
                if cur_dist > 0:
                    b += 1
                # Decrement right pointer
                else:
                    c -= 1
        return target - least_dist
