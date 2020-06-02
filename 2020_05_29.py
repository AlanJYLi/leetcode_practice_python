# 226. Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        root.left = r
        root.right = l
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            current.right, current.left = current.left, current.right
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return root

# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 2 > 0:
            return False
        else:
            return self.isPowerOfTwo(n // 2)

class Solution: # bit operation
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return n & (n-1) == 0

# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        val_list = []
        while head is not None:
            val_list.append(head.val)
            head = head.next
        
        return val_list == val_list[::-1]

# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # find the path
    def findPath(self, root, target):
        stack = [root]
        parent = {root: None}
        
        while target not in parent:
            curr = stack.pop(-1)
            if curr.left is not None:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right is not None:
                parent[curr.right] = curr
                stack.append(curr.right)
        
        path = []
        
        t = target
        while parent[t] is not None:
            path.append(t)
            t = parent[t]
        
        path.append(root)
        return path
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.findPath(root, p)
        path_q = self.findPath(root, q)
         
        for nood in path_p:
            if nood in path_q:
                return nood

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        anc = []
        
        def find(current_tree):
            if current_tree is None:
                return False
            
            left = find(current_tree.left)
            right = find(current_tree.right)
            
            if current_tree == p or current_tree == q:
                mid = True
            else:
                mid = False
            
            if mid+left+right >= 2:
                anc.append(current_tree)
            
            return mid or left or right
        
        find(root)
        return anc[0]

class Solution: # take advantage of binary search tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentval = root.val
        pval = p.val
        qval = q.val
        
        if parentval < min(pval, qval):
            return self.lowestCommonAncestor(root.right,p,q)
        elif parentval > max(pval, qval):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

# 237. Delete Node in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        store = {}
        for i in range(len(s)):
            ls = s[i]
            lt = t[i]
            if ls not in store:
                store[ls] = 1
            else:
                store[ls] += 1
            
            if lt not in store:
                store[lt] = -1
            else:
                store[lt] -= 1
        
        for l in store:
            if store[l] != 0:
                return False
        
        return True

# 243. Shortest Word Distance
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        best = len(words)
        anchor = ''
        target = ''
        for w in words:
            if w != word1 and w != word2 and anchor == '':
                continue
            if w == word1 and anchor == '':
                anchor = word1
                target = word2
                count = 0
                continue
            if w == word2 and anchor == '':
                anchor = word2
                target = word1
                count = 0
                continue
            if w == anchor:
                count = 0
                continue
            if w != word1 and w != word2 and anchor != '':
                count += 1
                continue
            if w == target:
                best = min(best, count+1)
                anchor, target = target, anchor
                count = 0
                continue
            
        return best

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1 = -1
        i2 = -1
        best = len(words)
        
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            if words[i] == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                best = min(best, abs(i1-i2))
        
        return best

# 246. Strobogrammatic Number
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pair = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        new = ''
        for s in num:
            if s not in pair:
                return False
            else:
                new = pair[s] + new
        
        return num == new

# 252. Meeting Rooms
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        
        timesort = sorted(intervals)
        for i in range(1,len(timesort)):
            if timesort[i][0] < timesort[i-1][1]:
                return False
        return True

# 256. Paint House
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        
        store = {}
        
        def paint(n,color):
            if (n, color) in store:
                return store[(n, color)]
            total = costs[n][color]
            if n == len(costs)-1:
                pass
            elif color == 0:
                total += min(paint(n+1,1), paint(n+1,2))
            elif color == 1:
                total += min(paint(n+1,0), paint(n+1,2))
            else:
                total += min(paint(n+1,0), paint(n+1,1))
            store[(n, color)] = total
            return total
        
        return min(paint(0,0), paint(0,1), paint(0,2))

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        
        import copy
        working_costs = copy.deepcopy(costs)
        for i in range(-1, -len(working_costs), -1):
            cost = working_costs[i]
            target = working_costs[i-1]
            target[0] = target[0] + min(cost[1], cost[2])
            target[1] = target[1] + min(cost[0], cost[2])
            target[2] = target[2] + min(cost[0], cost[1])
        
        return min(working_costs[0])

# 257. Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        
        stack = [root]
        pathmap = {root: None}
        pathlist = []
        
        while len(stack) > 0:
            current = stack.pop(-1)
            if current.left is not None:
                pathmap[current.left] = current
                stack.append(current.left)
            if current.right is not None:
                pathmap[current.right] = current
                stack.append(current.right)
            if current.left is None and current.right is None:
                target = current
                path = ''
                while pathmap[target] is not None:
                    path = '->' + str(target.val) + path
                    target = pathmap[target]
                path = str(root.val) + path
                pathlist.append(path)
        return pathlist

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def build(root, path):
            if root is not None:
                path = path + str(root.val)
                if root.left is None and root.right is None:
                    pathlist.append(path)
                else:
                    path = path + '->'
                    build(root.left, path)
                    build(root.right, path)
        
        pathlist = []
        build(root, '')
        return pathlist