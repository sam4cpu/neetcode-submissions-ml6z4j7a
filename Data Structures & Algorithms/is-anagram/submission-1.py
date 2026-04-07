class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for cc in t:
            count[ord(cc) - ord('a')] -= 1
        
        return all(p == 0 for p in count)
        