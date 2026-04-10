class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for l in s:
            count[l] += 1
        
        for i, n in enumerate(s):
            if count[n] == 1:
                return i
        return -1