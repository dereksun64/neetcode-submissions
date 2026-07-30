class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            out.append(str(len(s)))
            out.append("#")
            out.append(s)
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        out = []
        l = 0
        while r < len(s):
            r = l
            while r != "#":
                r += 1
            length = s[l:r]
            l = r + 1
            r = l + length
            word = s[l:r]
            out.append(word)
            l = r
        return out
            
