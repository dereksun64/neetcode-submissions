class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for str in strs:
            mapp = tuple(Counter(str))
            dic[mapp].append(str)
        
        out = []
        for key, strss in enumerate(dic):
            out.append([[s] for s in strss])
        
        return out