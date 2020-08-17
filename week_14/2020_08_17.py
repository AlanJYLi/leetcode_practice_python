# 361. Bomb Enemy
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        
        dp_l = [[0] * c for _ in range(r)] # 'e' on the left
        dp_r = [[0] * c for _ in range(r)] # 'e' on the right
        dp_u = [[0] * c for _ in range(r)] # 'e' above
        dp_b = [[0] * c for _ in range(r)] # 'e' below
        
        for i in range(r):
            t = 0
            for j in range(c):
                if grid[i][j] == 'E':
                    t += 1
                elif grid[i][j] == 'W':
                    t = 0
                else:
                    dp_l[i][j] = t
        
        for i in range(r):
            t = 0
            for j in range(c-1, -1, -1):
                if grid[i][j] == 'E':
                    t += 1
                elif grid[i][j] == 'W':
                    t = 0
                else:
                    dp_r[i][j] = t
        
        for j in range(c):
            t = 0
            for i in range(r):
                if grid[i][j] == 'E':
                    t += 1
                elif grid[i][j] == 'W':
                    t = 0
                else:
                    dp_u[i][j] = t
        
        for j in range(c):
            t = 0
            for i in range(r-1, -1, -1):
                if grid[i][j] == 'E':
                    t += 1
                elif grid[i][j] == 'W':
                    t = 0
                else:
                    dp_b[i][j] = t
        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    res = max(res, dp_l[i][j]+dp_r[i][j]+dp_u[i][j]+dp_b[i][j])
        return res

# 366. Find Leaves of Binary Tree
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def is_leaf(node):
            if node.left is None and node.right is None:
                return True
            else:
                return False
        
        def process(root):
            if root is None:
                return None
            
            if is_leaf(root):
                res.append([root.val])
                return None
            
            temp = []
            stack = [root]
            while len(stack) > 0:
                curr = stack.pop()
                if curr.left is not None:
                    if is_leaf(curr.left):
                        temp.append(curr.left.val)
                        curr.left = None
                    else:
                        stack.append(curr.left)
                if curr.right is not None:
                    if is_leaf(curr.right):
                        temp.append(curr.right.val)
                        curr.right = None
                    else:
                        stack.append(curr.right)
            res.append(temp[:])
            return root
        
        res = []
        while root is not None:
            root = process(root)
        return res

# 368. Largest Divisible Subset
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        nums.sort()
        store = {nums[0]: set()}
        store[nums[0]].add(nums[0])
        for i in range(1, len(nums)):
            val = nums[i]
            max_l = 0
            max_num = None
            for k in store:
                if val % k == 0:
                    if len(store[k]) > max_l:
                        max_l = len(store[k])
                        max_num = k
            store[val] = set()
            if max_num is None:
                store[val] = set()
                store[val].add(val)
            else:
                for ele in store[max_num]:
                    store[val].add(ele)
                store[val].add(val)
        
        max_l = 0
        max_num = None
        for k in store:
            if len(store[k]) > max_l:
                max_l = len(store[k])
                max_num = k
        return list(store[max_num])

