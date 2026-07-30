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
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j]
            print(length)
            i = j
            j = i + int(length)
            out.append(s[i:j])
            i = j
        return str(out)