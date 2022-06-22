class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # Iterate through nums
        for i, a in enumerate(nums):
            # Skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            # Create left and right pointers
            b = i+1
            c = n-1
            while b < c:
                s = a+nums[b]+nums[c]
                if s == 0:
                    # Add 3Sum
                    res.append([a,nums[b],nums[c]])
                    # Increment left pointer
                    b += 1
                    # Skip duplicates
                    while nums[b] == nums[b-1] and b<c:
                        b += 1
               # Increment left pointer
                elif s<0:
                    b += 1
                # Decrement right pointer
                else:
                    c -= 1
        return res