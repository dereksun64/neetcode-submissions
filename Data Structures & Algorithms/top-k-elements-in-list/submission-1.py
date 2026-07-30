class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)

        for num in nums:
            map[num] += 1
        
        print(map)
