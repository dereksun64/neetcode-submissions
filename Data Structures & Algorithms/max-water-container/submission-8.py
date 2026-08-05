class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amt = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            amt = max(amt, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
                continue
            r -= 1

        return amt
            