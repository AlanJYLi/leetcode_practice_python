# 413. Arithmetic Slices
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = 0
        i = 1
        j = i+1
        while j < len(A):
            diff = A[i]-A[i-1]
            if A[j] - A[j-1] == diff:
                j += 1
            else:
                l = (j-1)-(i-1)+1
                res += ((1+l-2)*(l-2-1+1))//2
                i = j
                j = i+1
        l = (j-1)-(i-1)+1
        res += ((1+l-2)*(l-2-1+1))//2
        return res

# 416. Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        else:
            t = total // 2
        n = len(nums)
        dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for j in range(1, t+1):
            dp[0][j] = False
        
        for i in range(1, n+1):
            for j in range(1, t+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][t]

# 417. Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix == []:
            return []
        
        r = len(matrix)
        c = len(matrix[0])
        
        seen_p = set()
        seen_a = set()
        
        def dfs_pacific(i, j):
            if (i,j) in seen_p:
                return
            seen_p.add((i,j))
            for h,v in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i = i+h
                new_j = j+v
                if 0<=new_i<r and 0<=new_j<c and matrix[new_i][new_j]>=matrix[i][j]:
                    dfs_pacific(new_i, new_j)
        
        def dfs_atlantic(i, j):
            if (i,j) in seen_a:
                return
            seen_a.add((i,j))
            for h,v in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i = i+h
                new_j = j+v
                if 0<=new_i<r and 0<=new_j<c and matrix[new_i][new_j]>=matrix[i][j]:
                    dfs_atlantic(new_i, new_j)
            
        for i in range(r):
            dfs_pacific(i,0)
            dfs_atlantic(i, c-1)
        for j in range(c):
            dfs_pacific(0,j)
            dfs_atlantic(r-1, j)
        
        return seen_p & seen_a

