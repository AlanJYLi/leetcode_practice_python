# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)

# 294. Flip Game II
class Solution:
    def canWin(self, s: str) -> bool:
        check = {}
        
        def process(s):
            if s in check:
                return check[s]
            for i in range(1, len(s)):
                if s[i-1] == '+' and s[i] == '+':
                    new = s[:i-1] +'--' + s[i+1:]
                    if process(new) == False:
                        check[s] = True
                        return True
            check[s] = False
            return False
        
        return process(s)

# 298. Binary Tree Longest Consecutive Sequence
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        def process(root, s):
            s.append(root.val)
            if root.left is None and root.right is None:
                res.append(s[:])
            if root.left is not None:
                process(root.left, s[:])
            if root.right is not None:
                process(root.right, s[:])
        
        def get_length(s):
            val = 1
            curr = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1] + 1:
                    curr += 1
                else:
                    val = max(val, curr)
                    curr = 1
            return max(val, curr)
            
        if root is None:
            return 0
        
        res = []
        process(root, [])
        val = 1
        for s in res:
            val = max(val, get_length(s))
        return val

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        self.res = 1
        
        def process(root, par_val, curr):
            if par_val is None:
                curr = 1
            else:
                if root.val == par_val + 1:
                    curr += 1
                else:
                    self.res = max(self.res, curr)
                    curr = 1

            if root.left is None and root.right is None:
                self.res = max(self.res, curr)
                return
            if root.left is not None:
                process(root.left, root.val, curr)
            if root.right is not None:
                process(root.right, root.val, curr)
            
        if root is None:
            return 0
        
        process(root, None, 1)
        return self.res

# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            temp = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp[i] = temp + 1
        return max(dp)

# 304. Range Sum Query 2D - Immutable
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cusum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    self.cusum[i][j] = matrix[0][0]
                elif j == 0:
                    self.cusum[i][j] = matrix[i][j] + self.cusum[i-1][j]
                elif i == 0:
                    self.cusum[i][j] = matrix[i][j] + self.cusum[i][j-1]
                else:
                    self.cusum[i][j] = matrix[i][j] + self.cusum[i][j-1] + self.cusum[i-1][j] - self.cusum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.cusum[row2][col2]
        elif row1 == 0 and col1 > 0:
            return self.cusum[row2][col2] - self.cusum[row2][col1-1]
        elif row1 > 0 and col1 == 0:
            return self.cusum[row2][col2] - self.cusum[row1-1][col2]
        else:
            return self.cusum[row2][col2] - self.cusum[row2][col1-1] - self.cusum[row1-1][col2] + self.cusum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
