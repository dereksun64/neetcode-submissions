class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[c] += 1
            m[tuple(count)] += s
        
        return list(m.values())