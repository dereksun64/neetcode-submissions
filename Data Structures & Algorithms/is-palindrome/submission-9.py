class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)

        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True