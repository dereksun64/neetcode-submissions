class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            out = max(out, (r-l)*(min(heights[r], heights[l])))
            if heights[l] <= heights[r]:
                l += 1
            else: r -= 1

        return out