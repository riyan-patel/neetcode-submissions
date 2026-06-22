class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i: [] for i in range(numCourses)}

        for c,p in prerequisites:
            preMap[c].append(p)
        
        visited = set()
        cycle = set()

        def dfs(c):
            
            if c in cycle:
                return False
            
            if c in visited:
                return True

            cycle.add(c)
            
            for p in preMap[c]:
                
                if not dfs(p): return False

            visited.add(c)
            cycle.remove(c)
            res.append(c)
            return True
        
        res = []
        for c in range(numCourses):
            if not dfs(c): return []
        return res
