class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [0]*len(nums)

        freq = Counter(nums)

        for key, c in freq.items():
            arr[c].append(key)

        out = []
        while len(out)<k:
            out.append(arr.pop())

        return out
