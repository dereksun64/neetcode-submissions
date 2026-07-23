class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        l = 0

        for num in nums:
            if num-1 in m:
                continue
            x= num
            temp = 1
            while x+1 in m:
                x+= 1
                temp += 1
            l = max(temp, l)

        return l