class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                result.append(i + 1)
                result.append((numbers.index(target - numbers[i])) + 1)
                return result
        return result