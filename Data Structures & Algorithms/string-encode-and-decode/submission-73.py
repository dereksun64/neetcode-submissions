class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s))
            out += "#"
            out += s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        l, r = 0, 0
        while l < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            word = s[l:r]
            out.append(word)
            l = r
        return out
