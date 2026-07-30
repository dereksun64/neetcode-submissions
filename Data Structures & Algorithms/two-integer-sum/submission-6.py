class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num

            if diff in mapp:
                return [mapp[diff], i]
            mapp.append([num, i])
        
        return False