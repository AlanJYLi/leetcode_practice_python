# 279. Perfect Squares
class Solution: # exceed time limit
    def numSquares(self, n: int) -> int:
        dp = {1:1, 2:2, 3:3, 4:1}
        if n <= 4:
            return dp[n]
        else:
            for num in range(5, n+1):
                val = floor(sqrt(num))
                if val**2 == num:
                    dp[num] = 1
                else:
                    h = val**2
                    l = num-h
                    minnum = float(inf)
                    while l <= h:
                        minnum = min(minnum, dp[h]+dp[l])
                        h -= 1
                        l += 1
                    dp[num] = minnum
            return dp[n]

class Solution:
    def numSquares(self, n: int) -> int:
        dp = {1:1, 2:2, 3:3, 4:1}
        is_square = [1, 4]
        if n <= 4:
            return dp[n]
        else:
            for num in range(5, n+1):
                val = floor(sqrt(num))
                if val**2 == num:
                    dp[num] = 1
                    is_square.append(num)
                else:
                    minnum = float(inf)
                    for temp in is_square:
                        minnum = min(minnum, dp[temp]+dp[num-temp])
                    dp[num] = minnum
            return dp[n]

# 280. Wiggle Sort
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(2, len(nums), 2):
            nums[i-1], nums[i] = nums[i], nums[i-1]

# 281. Zigzag Iterator
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        if self.v1 != []:
            self.from1 = True
        else:
            self.from1 = False

    def next(self) -> int:
        if self.from1 == True:
            if self.v2 != []:
                self.from1 = False
            return self.v1.pop(0)
        else:
            if self.v1 != []:
                self.from1 = True
            return self.v2.pop(0)        

    def hasNext(self) -> bool:
        if self.v1 == [] and self.v2 == []:
            return False
        else:
            return True
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

# 285. Inorder Successor in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        stack = []
        curr = root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr == p:
                if curr.right is not None:
                    temp = curr.right
                    while temp.left is not None:
                        temp = temp.left
                    return temp
                else:
                    if len(stack) > 0:
                        return stack[-1]
                    else:
                        return None
            else:
                curr = curr.right

# 286. Walls and Gates
class Solution: #dfs
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def dfs(i, j, count):
            if not (0<=i<len(rooms)) or not (0<=j<len(rooms[0])) or rooms[i][j]<count:
                return
            
            rooms[i][j] = min(count, rooms[i][j])
            dfs(i-1, j, count+1)
            dfs(i+1, j, count+1)
            dfs(i, j-1, count+1)
            dfs(i, j+1, count+1)
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
