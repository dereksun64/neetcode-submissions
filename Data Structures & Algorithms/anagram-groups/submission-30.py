class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            dic[tuple(Counter(s))].append(s)
        
        res = []

        for key, values in dic.items():
            a = []
            a.append(s for s in values)
            res.append(a)
        
        return res

