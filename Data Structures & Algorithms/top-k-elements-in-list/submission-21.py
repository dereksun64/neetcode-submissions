class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)

        for num in nums:
            map[num] += 1
        
        heap = []
        for key, value in map.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        out = []
        while heap:
            out.append(heapq.heappop(heap)[1])

        return out