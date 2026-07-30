class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c)-ord("a")] += 1

        for index, r in enumerate(s2):
            window[ord(r)-ord("a")] += 1

            if index >= len(s1):
                win[ord(r-len(s1))-ord("a")] -= 1
            
            if window == need: return True

        return False 
