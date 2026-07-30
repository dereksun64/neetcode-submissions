class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            fix = nums[i]
            l = i+1
            r = len(nums)-1

            while l < r:
                s = fix + l + r
                if s == 0:
                    out.append([fix, l, r])
                    l += 1
                    while nums[l] == nums[l-1]: l+= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return out