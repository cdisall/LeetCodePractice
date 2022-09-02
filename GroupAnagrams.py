class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        res = []
        for i in d:
            res.append(d[i])
        return res
