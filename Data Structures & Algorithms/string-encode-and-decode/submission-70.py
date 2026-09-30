class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s))
            out += "#"
            out += s

        return out

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        out = []
        while l < len(s):
            while s[r] != "#":
                r += 1
            length = s[l:r]
            print(length)
            l = r + 1
            r = l + int(length)
            word = s[l:r]
            out.append(word)
            l = r
        return out
