class Solution:

    def permute(self, nums):
        res = []
        if not nums:
            return res
        used = [0] * len(nums)
        perm = []
        self.rec_permute(nums, used, perm, res)
        return res

    def rec_permute(self, nums, used, perm, res):
        # Check if perm is complete
        if (len(perm) == len(nums)):
            res.append(perm)
            print(res)
            return
        # Add unused nums to perm
        for i, n in enumerate(nums):
            if used[i] == 1:
                continue
            used[i] = 1
            perm.append(nums[i])
            # Recurse to continue adding unused elements to perm
            self.rec_permute(nums, used, perm, res)
            del perm[len(perm) - 1]
            used[i] = 0
            print(1)

def main():
    s = Solution()
    l = [1,2,3]
    print(s.permute(l))

if __name__ == "__main__":
    main()

