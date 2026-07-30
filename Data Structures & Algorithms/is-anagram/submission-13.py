class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = defaultdict(int), defaultdict(int)

        for i in s:
            smap[i] += 1
        
        for i in t:
            tmap[t] += 1
        
        return smap != tmap