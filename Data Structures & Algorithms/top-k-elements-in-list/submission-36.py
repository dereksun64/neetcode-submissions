class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        table = []*(len(nums) + 1)
        for num, cnt in freq.items():
            table[cnt].append(num)
        
        res = []
        for i in range(len(table)-1, -1, -1):
            for num in i:
                while len(res) < k:
                    res.append()

            if len(res) == k:
                return res