class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)


        visited = set()

        def dfs(c):

            if c in visited:
                return False
            
            if preMap[c] == []:
                return True

            visited.add(c)

            for x in preMap[c]:
                if not dfs(x): return False
            visited.remove(c)
            preMap[c] = []
            return True
        

        for i in range(numCourses):
            if not dfs(i): return False
        return True
