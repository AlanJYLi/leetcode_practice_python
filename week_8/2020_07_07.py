# 1018. Binary Prefix Divisible By 5
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        if A == []:
            return []
        dp = [0]*len(A)
        dp[0] = A[0]
        res = [False]*len(A)
        res[0] = dp[0]%5==0
        for i in range(1,len(A)):
            dp[i] = (dp[i-1]<<1)+A[i]
            res[i] = dp[i]%5==0
        return res

# 1021. Remove Outermost Parentheses
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if S == '':
            return ''
        
        stack = []
        store = []
        for i in range(len(S)):
            if len(stack) > 1:
                if stack[-1][0] == '(' and S[i] == ')':
                    stack.pop()
                elif S[i] == '(':
                    stack.append([S[i],i])
            elif len(stack) == 1:
                if stack[-1][0] == '(' and S[i] == ')':
                    temp = stack.pop()
                    store.append(temp[1])
                    store.append(i)
                elif S[i] == '(':
                    stack.append([S[i],i])
            else:
                stack.append([S[i],i])
        res = S[:store[0]]
        for i in range(1,len(store)):
            res += S[store[i-1]+1:store[i]]
        return res

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        left = 0
        for s in S:
            if s == '(' and left > 0:
                res.append(s)
            if s == ')' and left > 1:
                res.append(s)
            
            if s == '(':
                left += 1
            else:
                left -= 1
        
        return ''.join(res)

# 1022. Sum of Root To Leaf Binary Numbers
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        res = []
        
        def process(root, path):
            if root:
                path = path + str(root.val)
                if root.left is None and root.right is None:
                    res.append(path)
                process(root.left, path)
                process(root.right, path)
        
        process(root, '')
        total = 0
        for s in res:
            total += int(s,2)
        return total

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def process(root, total):
            if root is None:
                return 0
            
            temp = total + root.val
            if root.left is None and root.right is None:
                return temp
            return process(root.left, 2*temp)+process(root.right, 2*temp)
        
        return process(root,0)

# 1025. Divisor Game
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] *(N+1)
        for i in range(2,N+1):
            for j in range(1,i):
                if i % j == 0:
                    dp[i] = dp[i] or not(dp[i-j])
        return dp[N]

# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        c = sorted(costs, key=lambda x: x[0]-x[1])
        
        n = len(c)//2
        total = 0
        for i in range(n):
            total += c[i][0]+c[i+n][1]
        return total
