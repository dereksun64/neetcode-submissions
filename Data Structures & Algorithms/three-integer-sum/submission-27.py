class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i>0 and num == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l<r:
                s = num + nums[l] + nums[r]
                if s == 0:
                    out.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif s >= 0:
                    r -= 1
                else:
                    l += 1
            
        return out