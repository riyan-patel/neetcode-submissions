class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_a = 0

        while l < r:

            h = min(heights[l], heights[r])
            w = r - l

            max_a = max(h * w, max_a)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_a



        