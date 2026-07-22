class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        zeroes = 0
        prod = 1
        for num in nums:
            if num: prod *= num
            else: zeroes += 1
        
        if zeroes > 1:
            return [0] * n
        
        res = [0] * n
        for i, k in enumerate(nums):
            if zeroes: 
                if k == 0: res[i] = prod
            else:
                res[i] = prod // k

        return res