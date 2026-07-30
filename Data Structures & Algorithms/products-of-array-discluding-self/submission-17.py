class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)

        # prefix
        pre = 1
        for i in range(len(nums)):
            pre *= nums[i-1]
            out[i] = out[i-1] * pre

        # postfix
        post = 1
        for i in range(len(nums), -1, -1):
            post *= nums[i+1]
            out[i] = out[i+1] * post
        
        return out

