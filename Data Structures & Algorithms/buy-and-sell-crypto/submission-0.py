class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1

        res = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                temp_p = prices[r] - prices[l]

                if temp_p > res:
                    res = temp_p
                r += 1
            
        return res
