class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for num in nums:
            if num in myset: return False
            else: myset.add(num)
        
        return True