class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        output = []

        for num in nums:
            map[num] += 1
        
        smap = sorted(map.values())

        for i in k:
            output.append(smap.pop())

        print(output)