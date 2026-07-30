class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [numbers[l], numbers[r]]
            elif sum >= target:
                r -= 1
            else:
                l += 1
        

