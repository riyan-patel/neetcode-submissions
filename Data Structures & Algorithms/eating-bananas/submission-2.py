class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k = r
        while l <= r:
            mid = (l + r) // 2
             
            temp_h = 0
            for i in piles:
                temp_h += math.ceil(i / mid)
            if temp_h > h:
                l = mid + 1
            elif temp_h <= h:
                r = mid - 1
                k = min(k, mid)
            
        return k
            
