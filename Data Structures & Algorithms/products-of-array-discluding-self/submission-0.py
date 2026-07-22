class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            prod = 1
            for a in range(0, i):
                prod *= nums[a]
            for b in range(i+1, len(nums)):
                prod *= nums[b]
            res[i] = prod
        
        return res