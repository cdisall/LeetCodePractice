class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        candidates.sort()

        def backtrack(t, i):
            if t < 1:
                return res.append(stack[:])
            else:
                while i < len(candidates) and t - candidates[i] > -1:
                    stack.append(candidates[i])
                    backtrack(t - candidates[i], i)
                    stack.pop()
                    i += 1
        backtrack(target, 0)
        return res