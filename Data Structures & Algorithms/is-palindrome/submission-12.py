class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for c in s:
            if c.isalnum(): a.append(c)
        
        t = "".join(a)

        l = 0 
        r = len(s)-1

        while l<r:
            if t[l].lower() != t[r].lower():
                return False
            l += 1
            r -= 1
        return True