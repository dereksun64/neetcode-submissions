class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = [[] for i in range(len(nums)+1)]

        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for num, cnt in count.items():
            table[cnt].append(num)
        
        res = []
        for col in range(len(table)-1, -1, -1):
            for num in col:
                res.append(num)
                if len(res) == k:
                    return res
        return res
