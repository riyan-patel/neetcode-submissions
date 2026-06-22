class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for i in range(len(nums)):
            if target - nums[i] in hashmap.keys() and i not in result and hashmap.get(target - nums[i]) not in result and i != hashmap.get(target - nums[i]):
                result.append(i)
                result.append(hashmap.get(target - nums[i]))
        return result