class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        dic = {i:[] for i in range(n)}
        
        for t, s in edges:
            dic[t].append(s)
            dic[s].append(t)
        
        visited = set()

        def dfs(t, prev):
            if t in visited:
                return False

            visited.add(t)


            for s in dic[t]:
                if s == prev:
                    continue
                if not dfs(s, t): return False
            
            return True
        

        return dfs(0, -1) and n == len(visited)


