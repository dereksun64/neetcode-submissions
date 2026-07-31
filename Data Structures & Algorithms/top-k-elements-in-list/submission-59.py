class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        out = []
        for f in range(len(freq) - 1, -1, -1):
            for num in freq[f]:
                out.append(num)
                if len(out) == k:
                    return out
        return out