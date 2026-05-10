class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        map = defaultdict(list)

        for s in strs:
            map[''.join(sorted(s))].append(s)
        
        out = []
        for key, value in map.items():
            out.append(value)
        
        return out