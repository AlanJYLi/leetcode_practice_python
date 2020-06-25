# 113. Path Sum II
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res = []
        
        def process(root, t, path):
            if root.val == t and root.left is None and root.right is None:
                path = path + [root.val]
                res.append(path[:])
            else:
                path = path + [root.val]
                if root.left is not None:
                    process(root.left, t-root.val, path)
                if root.right is not None:
                    process(root.right, t-root.val, path)
        
        if root is None:
            return []
        process(root, sum, [])
        return res

# 114. Flatten Binary Tree to Linked List
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        lt = self.flatten(root.left)
        rt = self.flatten(root.right)
        
        if lt is not None:
            lt.right = root.right
            root.right = root.left
            root.left = None
        return rt if rt is not None else lt

# 115. Distinct Subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t):
            return 0
        elif len(s) == len(t):
            return 1 if s==t else 0
        else:
            store = {}
            def process(i, j):
                M, N = len(s), len(t)
                if i == M or j == N or M - i < N - j:
                    return int(j == len(t))
            
                if (i, j) in store:
                    return store[(i,j)]
            
                res = process(i + 1, j)
                if s[i] == t[j]:
                    res += process(i + 1, j + 1)
            
                store[(i,j)] = res
                return res        
            
            return process(0,0)

# 116. Populating Next Right Pointers in Each Node
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = [root]
        while len(queue)>0:
            n = len(queue)
            for i in range(n):
                curr = queue.pop(0)
                if i == n-1:
                    curr.next = None
                else:
                    curr.next = queue[0]
                if curr.left is not None:
                    queue.append(curr.left)
                    queue.append(curr.right)
        return root

# 117. Populating Next Right Pointers in Each Node II
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = [root]
        while len(queue)>0:
            n = len(queue)
            for i in range(n):
                curr = queue.pop(0)
                if i == n-1:
                    curr.next = None
                else:
                    curr.next = queue[0]
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return root

# 120. Triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

# 123. Best Time to Buy and Sell Stock III
class Solution: # exceed time limit
    def maxProfit(self, prices: List[int]) -> int:
        
        def onetime(s):
            if len(s) <= 1:
                return 0
            curr_min = s[0]
            profit = 0
            for i in range(1,len(s)):
                val = s[i]
                if val < curr_min:
                    curr_min = val
                else:
                    if val - curr_min > profit:
                        profit = val - curr_min
            return profit
        
        res = onetime(prices)
        if len(prices) < 4:
            return res
        else:
            for i in range(2, len(prices)-1):
                left = prices[:i]
                right = prices[i:]
                res = max(res, onetime(left)+onetime(right))
            return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
             
        left = [0]*len(prices) # store the max res from prices[0] to prices[i]
        right = [0]*len(prices) # store the max res from prices[i+1] to pirces[-1]
        
        lmin = prices[0]
        rmax = prices[-1]
        
        for i in range(1,len(prices)):
            left[i] = max(left[i-1], prices[i]-lmin)
            lmin = min(lmin, prices[i])
            
            j = len(prices)-1-i
            right[j] = max(right[j+1], rmax-prices[j])
            rmax = max(rmax, prices[j])
        
        res = left[0]+right[1]
        for i in range(1, len(prices)-1):
            res = max(res, left[i]+right[i+1])
        return max(res,left[-1])

class Solution: # smart way in leetcode
    '''
    The intuition is that we can consider the problem as a game, and we as agent could make at most two transactions 
    in order to gain the maximum points (profits) from the game. The two transactions be decomposed into 4 actions: 
    "buy of transaction #1", "sell of transaction #1", "buy of transaction #2" and "sell of transaction #2". 
    To solve the game, we simply run a simulation along the sequence of prices, at each time step, 
    we calculate the potential outcomes for each of our actions. At the end of the simulation, 
    the outcome of the final action "sell of transaction #2" would be the desired output of the problem.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost = float('inf')
        t2_cost = float('inf')
        t1_profit = 0
        t2_profit = 0
        
        for p in prices:
            t1_cost = min(p, t1_cost)
            t1_profit = max(p-t1_cost,t1_profit)
            t2_cost = min(p-t1_profit, t2_cost)
            t2_profit = max(p-t2_cost, t2_profit)
        
        return t2_profit

# 124. Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        
        def process(root):
            if root is None:
                return 0
            
            l_add = max(process(root.left),0)
            r_add = max(process(root.right),0)
            
            temp = root.val+l_add+r_add
            self.res = max(self.res, temp)
            return root.val+max(l_add,r_add)
        
        process(root)
        return self.res