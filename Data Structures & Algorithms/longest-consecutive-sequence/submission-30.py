class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        longest = 1

        for n in s:
            if n-1 not in s:
                length = 1
                while n+length in s:
                    length += 1
                    longest = max(length, longest)
        return longest