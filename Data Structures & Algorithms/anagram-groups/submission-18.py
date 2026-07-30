class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for str in strs:
            mapp = Counter(str)
            dic[mapp.tuple()].append(str)
        
        out = []
        for key, strss in dic:
            out.append([[s] for s in strss])
        
        return out