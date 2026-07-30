class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]

        freq = Counter(nums)

        for key, c in freq.items():
            arr[c].append(key)

        out = []
        for i in range(len(nums)+1, 0, -1):
            for num in arr[i]:
                out.append(num)
                if len(out) == k:
                    return out



