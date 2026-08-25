class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0

        while r < len(s):
            l = r
            while s[r] != "#":
                r+=1
            length = int(s[l:r])
            res.append(s[r + 1: r + 1 + length])
            r = r + 1 + length
        return res
            

