class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cleaned = sorted(set(nums))

        out = ()

        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    out.append([num, nums[l], nums[r]])
                elif sum >= 0:
                    r -= 1
                else:
                    l += 1
        
        return out
