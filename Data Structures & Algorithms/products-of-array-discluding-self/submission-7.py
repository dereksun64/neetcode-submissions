class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)

        # pre
        for i, num in enumerate(nums):
            if i == 0: continue
            out[i] = out[i-1]*nums[i-1]
        
        # post
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = postfix
            postfix *= nums[i]
        
        return out