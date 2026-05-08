class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict stores i of nums[i]
        dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in dict:
                return [dict[nums[i]], i]

            dict[difference] = i