# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        res = []

        queue.append(root)


        while queue:

            rightside = None

            qlen = len(queue)

            for i in range(qlen):

                node = queue.popleft()

                if node:
                    rightside = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightside:
                res.append(rightside.val)
            
        return res

        
        

