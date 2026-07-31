class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        big = 0
        while l < r:
            area = (r - l)*min(heights[l], heights[r])
            big = max(big, area)
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return big