class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target, window = [0]*26, [0]*26

        for i, s in enumerate(s1):
            target[ord(s)-ord("a")] += 1
        
        l = 0
        for r, s in enumerate(s2):
            window[ord(s)-ord("a")] += 1
            if r > len(s1)-1:
                window[ord(s2[l])-ord("a")] -= 1
                l += 1
            
            if window == target: return True
        return False