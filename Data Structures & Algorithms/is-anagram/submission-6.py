class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sCount = [0]*26
        tCount = [0]*26

        for i in range(len(s)):
            sCount[ord(s[i])-ord("a")]
            tCount[ord(t[i])-ord("a")]
        
        return sCount == tCount