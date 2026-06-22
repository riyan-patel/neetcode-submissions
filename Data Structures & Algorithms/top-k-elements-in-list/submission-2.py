class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for num, count in hashmap.items():
            freq[count].append(num)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
