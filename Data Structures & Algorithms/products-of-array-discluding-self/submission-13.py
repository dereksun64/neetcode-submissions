class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)

        # prefix
        pre = 1
        for i in range(len(nums)):
            if i < 1:
                continue
            out[i] = out[i-1] * pre
            pre *= nums[i]

        # postfix
        post = 1
        for i in range(len(nums), -1, -1):
            if i > len(nums) - 1:
                continue
            out[i] = out[i+1] * post
            post *= nums[i]
        
        return out