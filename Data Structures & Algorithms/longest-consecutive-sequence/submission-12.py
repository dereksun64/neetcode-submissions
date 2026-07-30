class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        m = set()
        
        for r in range(len(nums)):
            if nums[r] - 1 in m:
                m.add(nums[r])
                longest = max(longest, len(m))
            m.clear()
            m.add(nums[r])

        return longest
