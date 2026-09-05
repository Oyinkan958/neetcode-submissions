class Solution:

    def encode(self, strs: List[str]) -> str:
        end = []
        for s in strs:
            end.append(str(len(s)))
            end.append("#")
            end.append(s)
        return "".join(end)

    def decode(self, s: str) -> List[str]:
        end =[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            end.append(s[i:j])
            i = j
        return end
