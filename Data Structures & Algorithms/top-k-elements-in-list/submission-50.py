class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] += 1
        
        out = []
        for i in range(len(freq)-1, -1, -1):
            for s in freq[i]:
                out.append(s)
                if len(out) == k:
                    return out
                
        
        