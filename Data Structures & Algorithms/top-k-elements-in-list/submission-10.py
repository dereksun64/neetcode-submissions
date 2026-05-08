class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        arr = []
        for number, c in count.items():
            arr.append([c, number])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res