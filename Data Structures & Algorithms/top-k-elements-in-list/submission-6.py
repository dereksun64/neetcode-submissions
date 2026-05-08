class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        output = []

        for num in nums:
            map[num] += 1
        
        array = []
        for num, freq in map.items():
            array.append([freq, num])
        array.sort()

        for i in range(k):
            output.append(array.pop()[1])

        return output