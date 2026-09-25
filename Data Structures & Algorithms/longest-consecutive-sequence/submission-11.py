class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)

        res = 0


        for i in range(len(nums)):


            if (nums[i] - 1) not in numset:
                lenght = 0

                while (nums[i] + lenght) in numset:
                    lenght += 1
                

                res = max(res, lenght)
        
        return res
            

            
       


