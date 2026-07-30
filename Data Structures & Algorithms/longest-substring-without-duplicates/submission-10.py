class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        a = set()
        l = 0
        for r, num in s.items():
            while num in a:
                a.remove(s[l])
                l += 1
            a.add(num)

            longest = max(longest, len(a))

        return longest
