class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for c in strs:
            sortedS = ''.join(sorted(c))
            map[sortedS].append(c)
        return list(map.values())




