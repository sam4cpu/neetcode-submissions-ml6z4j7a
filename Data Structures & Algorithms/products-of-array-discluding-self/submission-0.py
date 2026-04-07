class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prod = 0

        for i in range(n):
            prod = 1
            for j in range(n):
                if j == i:
                    continue
                prod *= nums[j]
            res.append(prod)
        return res
        