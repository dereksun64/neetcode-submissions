class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        table = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq.items():
            table[cnt].append(num)
        
        res = []
        for i in range(len(table)-1, -1, -1):
            for num in table[i]:
                res.append(num)
                if len(res) == k:
                    return res