class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = []
        for num in nums:
            if num in c:
                return True
            c.append(num)
        return False