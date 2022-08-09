class Solution:
    
    def rec_permute(self, nums, used, perm, res):
        # Check if perm is complete
        if (len(perm) == len(nums)):
            res.append(perm)
            return
        # Add unused nums to perm
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = 1
            perm.append(nums[i])
            # Recurse to continue adding unused elements to perm
            self.rec_permute(nums, used, perm, res)
            del perm[-1]
            used[i] = 0
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        used = [0] * len(nums)
        perm = []
        self.rec_permute(nums, used, perm, res)
        return res





