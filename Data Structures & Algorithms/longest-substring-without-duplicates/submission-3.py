class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        p = set()
        for r in range(len(s)):
            while s[r] in p:
                p.remove(s[l])
                l += 1
            p.add(s[r])
            res = max(res, r - l + 1)
        return res



        