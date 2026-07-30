class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm = "".join(char.lower() for c in s if c.isalnum())

        l = 0
        r = len(norm) - 1

        while l < r:
            if norm[l] != norm[r]:
                return False
            l += 1
            r -= 1
        return True