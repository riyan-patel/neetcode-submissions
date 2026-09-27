class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for i in range(len(triplets)):

            f = triplets[i][0]
            s = triplets[i][1]
            t = triplets[i][2]

            if f > target[0] or s > target[1] or t > target[2]:
                continue
            
            for j, v in enumerate(triplets[i]):
                if v == target[j]:
                    good.add(j)
        return len(good) == 3
        