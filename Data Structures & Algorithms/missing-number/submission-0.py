class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        #res = 3

        for i in range(len(nums)):

            res += (i - nums[i])
        
        return res



        




        