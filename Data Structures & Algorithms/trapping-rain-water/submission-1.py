class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                if maxL - height[l] > 0:
                    res += (maxL - height[l])
                l += 1
                maxL = max(maxL, height[l])
            else:
                if maxR - height[r] > 0:
                    res += (maxR - height[r])
                r -= 1
                maxR = max(maxR, height[r])
        return res






       
