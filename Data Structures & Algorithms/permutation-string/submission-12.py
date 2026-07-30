class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        target, window = [0]*26, [0]*26
        size = len(s1)

        for c in s1:
            target[ord(c) - ord("a")] += 1
        
        for r in range(len(s2)):
            window[ord(s2[r]) - ord("a")] += 1

            if r > size:
                l = s2[r - size]
                window[ord(s2[l]) - ord("a")] -= 1
            
            if window == target: return True

        return False