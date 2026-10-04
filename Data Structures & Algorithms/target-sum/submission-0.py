class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            nextdp = defaultdict(int)
            for curr_sum, count in dp.items():

                nextdp[curr_sum + nums[i]] += count
                nextdp[curr_sum - nums[i]] += count
            dp = nextdp

        return dp[target]


        