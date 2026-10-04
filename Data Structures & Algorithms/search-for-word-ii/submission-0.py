class TrieNode():

    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self,word):

        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for w in words:

            root.addword(w)

        
        Rows = len(board)
        cols = len(board[0])

        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if (r not in range(Rows) or c not in range(cols) or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]

            word += board[r][c]
            if node.isword:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c))
        
        for r in range(Rows):
            for c in range(cols):

                dfs(r,c,root,"")
        
        return list(res)


        