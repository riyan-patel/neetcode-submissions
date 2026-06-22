class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {i: [] for i in range(n)}

        for n1, n2 in edges:
            dic[n1].append(n2)
            dic[n2].append(n1)
        

        visited = set()

        def dfs(n):

            if n in visited:
                return
            
            visited.add(n)

            for s in dic[n]:
                dfs(s)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count



