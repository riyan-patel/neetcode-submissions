class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(lst):
            r1, r2 = 0,0

            for n in lst:
                temp = max(r1 + n, r2)
                r1 = r2
                r2 = temp
            
            return r2
        
        start = help(nums[:-1])
        end = help(nums[1:])

        return max(start, end, nums[0])