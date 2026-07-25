class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = defaultdict(int), defaultdict(int)

        for c in s:
            smap[c] += 1
        for c in t:
            tmap[c] += 1
        
        return smap == tmap