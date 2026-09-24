class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # build adj list

        adj = {c : set() for w in words for c in w}

        for i in range(len(words)-1):

            w1 = words[i]
            w2 = words[i + 1]

            minlen = min(len(w2), len(w1))

            if len(w2) < len(w1) and w1[:minlen] == w2[:minlen]:
                return ""
            
            for j in range(minlen):
                if w1[j] != w2[j]:

                    adj[w1[j]].add(w2[j])
                    break
        

        visit = {}

        res = []

        def dfs(c):

            if c in visit:
                return visit[c]

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)