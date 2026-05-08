class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):
            j = target - nums[i]

            if j in map:
                return [map[j], i]

            map[nums[i]] = i
            