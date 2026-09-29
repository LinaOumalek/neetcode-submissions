class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            num = ""
            for char in s:
                if char == "#":
                    break
                num += char
            start= len(num)+1
            num = int(num)
            res.append(s[start:start+num])
            s = s[start+num:]
        return res


