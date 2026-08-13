class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            wrd = str(len(s)) + "#" + s
            res.append(wrd)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            res.append(s[j + 1: j + length + 1])
            i = j + length + 1
        print("dec", res)
        return res
