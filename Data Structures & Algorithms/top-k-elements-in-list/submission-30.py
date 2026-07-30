class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = []
        for num, cnt in freq:
            heapq.heappush(heap, [cnt, num])
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for a in heap:
            res.append(a)