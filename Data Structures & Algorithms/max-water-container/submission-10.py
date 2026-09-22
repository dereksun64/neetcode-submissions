class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0

        l = 0
        r = len(heights)-1

        while l<r:
            out = max(out, (min(heights[l], heights[r])*(r-l)))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return out