class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + s for s in res]
        return res
def main():
     s = Solution()
     print(s.subsets([1,4,5,8])
if __name__ == "__main__":
     main()
