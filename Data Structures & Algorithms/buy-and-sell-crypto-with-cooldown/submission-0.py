class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # state buying or sellin 
        # if buying increae i by 1
        # if selling incrase i by 2 bceuase need a cooldown day

        dp = {} # key = (i, buying (bool))



        def dfs(i, buying):

            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)

                dp[(i, buying)] = max(buy, cooldown)
            else:

                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)

                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]

        return dfs(0, True)