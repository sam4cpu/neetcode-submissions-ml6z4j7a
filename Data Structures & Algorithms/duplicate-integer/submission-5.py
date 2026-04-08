class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = []
        for n in nums:
            if n in c:
                return True
            c.append(n)
        return False