class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def rob1(arr):

            r1 = 0
            r2 = 0

            for n in arr:
                temp = max(r1 + n, r2)

                r1 = r2
                r2 = temp
            
            return r2
        
        start = rob1(nums[:-1])
        end = rob1(nums[1:])

        return max(start, end, nums[0])
