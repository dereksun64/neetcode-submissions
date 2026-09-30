class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for a in s:
            map[a] += 1
        for b in t:
            map[b] -= 1

        for v in map.values():
            if v != 0:
                return False
        return True