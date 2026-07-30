class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cleaned = list(dict.fromkeys(nums.sort()))
        print(cleaned)
