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
        r = 0

        while r < len(s):
            l = r
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            word = s[l:r]
            out.append(word)
        return out