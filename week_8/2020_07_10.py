# 236. Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        store = {root:None}
        while p not in store or q not in store:
            curr = stack.pop()
            if curr.left is not None:
                store[curr.left] = curr
                stack.append(curr.left)
            if curr.right is not None:
                store[curr.right]= curr
                stack.append(curr.right)
        parent = set()
        while p is not None:
            parent.add(p)
            p = store[p]
        while q not in parent:
            q = store[q]
        return q

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        
        def process(root):
            if root is None:
                return False
            inleft = process(root.left)
            inright = process(root.right)
            isself = root == p or root == q
            if inleft + inright + isself >= 2:
                self.res = root
            return inleft or inright or isself
        
        process(root)
        return self.res

# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_to_right = [0]*n
        right_to_left = [0]*n
        
        for i in range(n):
            if i == 0:
                left_to_right[i] = nums[i]
                right_to_left[n-i-1] = nums[n-i-1]
            else:
                left_to_right[i] = nums[i]*left_to_right[i-1]
                right_to_left[n-i-1] = nums[n-i-1]*right_to_left[n-i]
        
        res = [0]*n
        for i in range(n):
            if i == 0:
                res[i] = right_to_left[i+1]
            elif i == n-1:
                res[i] = left_to_right[i-1]
            else:
                res[i] = left_to_right[i-1]*right_to_left[i+1]
        return res

# 240. Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        r = len(matrix)
        c = len(matrix[0])
        
        i = r-1
        j = 0
        while j<c and i>=0:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

# 1085. Sum of Digits in the Minimum Number
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        val = min(A)
        return int(sum([int(i) for i in list(str(val))])%2 == 0)

# 1086. High Five
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        store = {}
        for i, s in items:
            if i not in store:
                store[i] = [s]
            else:
                store[i].append(s)
        res = []
        for i in store:
            val = store[i]
            if len(val) <= 5:
                avg = sum(val)//len(val)
            else:
                val.sort(reverse=True)
                avg = sum(val[0:5])//5
            res.append([i,avg])
        
        return sorted(res, key=lambda x:x[0])
