class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            smap[s[i]] += 1
            tmap[t[i]] += 1
        
        return smap == tmap