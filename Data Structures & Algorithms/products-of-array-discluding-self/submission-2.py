class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prod = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                prod *= num

        if zeroes > 1:
            return [0]*n
        
        res = [0]*n
        
        if zeroes == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    res[i] = prod
            return res

        for i in range(n):
            res[i] = prod//nums[i]
        
        return res
