class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0]*26

        for s in s1:
            freq1[ord(s)-ord("a")] += 1
        
        for i in range(len(s2)):
            window = s2[i:i+len(s1)]
            freq2 = [0]*26

            for w in window: 
                freq2[ord(w)-ord("a")] += 1

            if freq2 == freq1: 
                return True

        return False