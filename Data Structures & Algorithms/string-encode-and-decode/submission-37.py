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
        while l < len(s):
            r = l
            while r != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            out.append(s[l:r])
        return out
        