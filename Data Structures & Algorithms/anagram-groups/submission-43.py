class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for i, str in enumerate(strs):
            count = [0]*26
            for c in str:
                count[c] += 1
            table[tuple(count)].append(str)
        
        return list(table.values())