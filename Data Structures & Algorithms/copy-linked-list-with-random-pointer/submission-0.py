"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        oldNew = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldNew[curr] = copy
            curr = curr.next
        

        curr = head
        while curr:
            c = oldNew[curr]
            c.next = oldNew[curr.next]
            c.random = oldNew[curr.random]

            curr = curr.next

        return oldNew[head]





