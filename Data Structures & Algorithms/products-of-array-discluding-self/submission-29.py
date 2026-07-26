class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)

        # pre
        pre = 1
        for i, num in enumerate(nums):
            out[i] = pre
            pre *= num
        
        # post
        post = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= post
            post *= nums[i]
        
        return out