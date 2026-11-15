class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += '#'
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j != len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            i = j
            j += length
            res.append(s[i:j])
            i = j
        return res
        
        
