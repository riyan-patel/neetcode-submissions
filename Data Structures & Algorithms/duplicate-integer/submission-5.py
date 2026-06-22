class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        temp = set(nums)

        return not (len(nums) == len(temp))