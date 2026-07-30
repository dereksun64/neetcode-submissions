class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0)
        
        arr = []
        for y, v in cnt.items():
            arr.append([v, y])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res