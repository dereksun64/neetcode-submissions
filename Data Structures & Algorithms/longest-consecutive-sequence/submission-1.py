class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        sort = sorted(nums)

        diff = [0] * len(sort)

        for i in range(1, len(sort)):
            diff[i] = sort[i] - sort[i-1]
        
        longest = 0
        temp = 1

        for i in range(len(diff)):
            if diff[i] == 1:
                temp += 1
            elif diff[i] == 0:
                continue
            else:
                if longest < temp:
                    longest = temp
                temp = 1

        if longest < temp:
            longest = temp
        
        return longest
