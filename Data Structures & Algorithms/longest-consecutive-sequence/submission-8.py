class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0

        m = set()

        longest = 0

        for r in range(len(nums)):
            if nums[r] in m:
                m.remove(nums[l])
                l += 1
                while l<r and nums[l + 1] == nums[l]:
                    l += 1
            m.add(nums[r])
            longest = max(longest, len(m))
        return longest
