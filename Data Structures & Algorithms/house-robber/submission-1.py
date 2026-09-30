class Solution:
    def rob(self, nums: List[int]) -> int:
        #[2,9,8,3,6]
        # rob1 = 2, rob2 = 0
        # temp = 2
        # rob1 = 0
        # rob2 = 2

        # r1 = 0 r2 = 2
        # n = 9
        # temp = 9, 2
        # r1 = 2
        # r2 = 9


        # n = 8
        # r1 = 2
        # r2 = 9
        # temp = r1 + n, r2
        # temp = 10, 9 = 10
        # r1 = 9
        # r2 = 10
        
        r1 = 0
        r2 = 0

        for n in nums:
            temp = max(r1 + n, r2)
            r1 = r2
            r2 = temp
        return r2
