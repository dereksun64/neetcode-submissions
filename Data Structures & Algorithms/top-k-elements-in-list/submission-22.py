class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1

        freq = [[] for i in range(len(nums)+1)]
        for num, count in map.items():
            freq[count].append(num)
        
        out = []
        for i in range(len(freq)-1, 0, -1):
            for value in freq[i]:
                out.append(value)
                if len(out) == k:
                    return out