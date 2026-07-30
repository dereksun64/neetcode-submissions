class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        longest = 0
        
        s = set()
        l = 0
        for r, num in s:
            while num in s:
                s.remove(s[l])
                l += 1
            s.add(num)

            longest = max(longest, len(set))

        return longest
