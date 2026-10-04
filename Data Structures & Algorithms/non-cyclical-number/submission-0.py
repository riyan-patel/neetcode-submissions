class Solution:
    def isHappy(self, n: int) -> bool:


        visit = set()

        while n not in visit:

            visit.add(n)
            n = self.sumofsquare(n)

            if n == 1:
                return True
        
        return False
    

    def sumofsquare(self, n):

        output = 0

        while n:

            d = n % 10
            d = d ** 2
            output += d
            n = n // 10
        return output
        