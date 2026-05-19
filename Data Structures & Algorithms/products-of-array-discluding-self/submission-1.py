class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 0
        ans = []
        
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            ans.append(prod)
        return ans
    
             
        
        

        