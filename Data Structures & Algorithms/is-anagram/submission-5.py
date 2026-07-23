class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False
        

        s_f = {}
        t_f = {}
        for i in range(len(s)):
            s_f[s[i]] = s_f.get(s[i], 0) + 1
            t_f[t[i]] = t_f.get(t[i], 0) + 1

        
        return s_f == t_f
