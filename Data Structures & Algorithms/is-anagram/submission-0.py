class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        a = {}
        
        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1
            a[t[i]] = a.get(t[i], 0) - 1

        for i in a:
            if a[i] != 0:
                return False
        return True