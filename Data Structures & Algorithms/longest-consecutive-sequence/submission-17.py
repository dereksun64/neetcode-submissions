class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        length = 0

        for num in nums:
            if num-1 not in s:
                while num + length in s:
                    length += 1
                    max(longest, length)
        return longest