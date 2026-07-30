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
        i = 0
        for c in s:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j
            j = 1+length
            out.append(s[i,j])
            i = j
        return str(out)