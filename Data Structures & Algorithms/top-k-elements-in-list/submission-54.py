class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for num, cnt in freq.items():
            buckets[cnt].append(num)

        out = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                out.append(num)
                if len(out) == k:
                    return out