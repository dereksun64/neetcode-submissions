class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cleaned = sorted(set(nums))
        print(cleaned)
