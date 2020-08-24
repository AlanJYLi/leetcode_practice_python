# 429. N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        while len(queue) > 0:
            n_tree = len(queue)
            temp = []
            for _ in range(n_tree):
                tree = queue.pop(0)
                temp.append(tree.val)
                for c in tree.children:
                    queue.append(c)
            res.append(temp)
        return res

# 430. Flatten a Multilevel Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        
        dummy = Node(0, None, head, None)
        prev = dummy
        stack = [head]
        while len(stack) > 0:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            
            if curr.next is not None:
                stack.append(curr.next)
            if curr.child is not None:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        dummy.next.prev = None
        return dummy.next

