class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cleaned = list(dict.fromkeys(nums))
        print(cleaned)
