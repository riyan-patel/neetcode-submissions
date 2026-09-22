class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            temp = len(i)
            res += str(temp)
            res += "#"
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j]) # get the num before "#"
            start = j + 1
            end = j + 1 + lenght
            temp_res = s[start:end]
            res.append(temp_res)
            i = j + 1 + lenght
        return res








        
