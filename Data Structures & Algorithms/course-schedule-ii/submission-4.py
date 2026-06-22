class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)


        visited = set()
        cycle = set()

        def dfs(c):

            if c in visited:
                return True
            
            if c in cycle:
                return False

            cycle.add(c)

            for x in preMap[c]:
                if not dfs(x): return False
            visited.add(c)
            cycle.remove(c)
            res.append(c)
            return True
        
        res = []
        for i in range(numCourses):
            if not dfs(i): return []
        return res
