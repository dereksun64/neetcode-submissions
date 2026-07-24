class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        length = len(s1)
        l = 0
        for r in range(length-1, len(s2)):
            if Counter(s2[l:r+1]) == Counter(s1):
                return True
            l+= 1
        return False