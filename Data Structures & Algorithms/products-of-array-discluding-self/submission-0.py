class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        original = nums
        for i in range(len(nums)):
            temp = original[:]
            temp.pop(i)
            product = 1
            for num in temp:
                product *= num
            res[i] = product
        
        return res