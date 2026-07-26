class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]

        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1
        
        for num, cnt in counter.items():
            freq[cnt].append(num)
        
        out = []
        for i in range(len(freq)-1, -1, -1):
            for c in freq[i]:
                out.append(c)
                if len(out) == k:
                    return out