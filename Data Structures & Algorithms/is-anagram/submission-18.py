class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = defaultdict(int), defaultdict(int)
        for a in s:
            smap[a] += 1
        for b in t:
            tmap[b] += 1

        return smap == tmap