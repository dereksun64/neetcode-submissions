class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        table = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            table[cnt].append(num)

        out = []
        for i in range(len(table)-1, -1, -1):
            for num in table[i]:
                out.append(num)
                if len(out) == k:
                    return out