class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        res = 0
        cset = set()

        for i in range(len(s)):


            while s[i] in cset:
                cset.remove(s[l])
                l += 1
            
            cset.add(s[i])

            res = max(res, i - l + 1)
        return res


        