# 188. Best Time to Buy and Sell Stock IV
class Solution: # similar with Best Time to Buy and Sell Stock III
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if k == 0:
            return 0
        if k >= len(prices)//2:
            res = 0
            for i in range(1, len(prices)):
                res += max(prices[i]-prices[i-1],0)
            return res
        
        cost = [float('inf')] * k
        profit = [0] * k
        for p in prices:
            cost[0] = min(cost[0], p)
            profit[0] = max(profit[0], p-cost[0])
            for i in range(1,k):
                cost[i] = min(cost[i], p-profit[i-1])
                profit[i] = max(profit[i], p-cost[i])
        return profit[-1]

# 199. Binary Tree Right Side View
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                curr = queue.pop(0)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                if i == n-1:
                    res.append(curr.val)
        return res

# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        
        
        def dfs(r, c):
            grid[r][c] = '0'
            if r-1 >= 0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            if r+1 < R and grid[r+1][c] == '1':
                dfs(r+1, c)
            if c-1 >= 0 and grid[r][c-1] == '1':
                dfs(r, c-1)
            if c+1 < C and grid[r][c+1] == '1':
                dfs(r, c+1)
        
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

# 201. Bitwise AND of Numbers Range
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        while len(bin(m)) == len(bin(n)) and m != 0:
            p = len(bin(m))-2
            res += 2**(p-1)
            m = m-2**(p-1)
            n = n-2**(p-1)
        return res

# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        store = {}
        for pair in prerequisites:
            curr = pair[0]
            prev = pair[1]
            if prev not in store:
                store[prev] = [curr]
            else:
                store[prev].append(curr)
        
        
        def cycle(curr, store, check, path):
            if check[curr]:
                return False
            if path[curr]:
                return True
            
            path[curr] = True
            temp = False
            if curr in store:
                for prev in store[curr]:
                    temp = cycle(prev, store, check, path)
                    if temp == True:
                        break
            path[curr] = False
            check[curr] = True
            return temp
        
        check = [False]*numCourses
        path = [False]*numCourses
        for curr in range(numCourses):
            if cycle(curr, store, check, path):
                return False
        return True

# 208. Implement Trie (Prefix Tree)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.w = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for i in range(1,len(word)):
            s = word[:i]
            if s not in self.w:
                self.w[s] = 1
        self.w[word] = 2
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.w and self.w[word] == 2
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.w

