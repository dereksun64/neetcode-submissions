class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return False
        myset = set(nums)
        l = 1

        for i in myset:
            if i-1 in myset:
                continue
            curr = 1
            while i + curr in myset:
                curr += 1
            l = max(curr, l)
        return l
