class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            adj[c].append(p)


        visit = set()


        def dfs(c):

            if c in visit:
                return False

            if adj[c] == []:
                return True
            
            visit.add(c)

            for i in adj[c]:
                if not dfs(i):
                    return False
            visit.remove(c)
            adj[c] = []
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True



