# 606. Construct String from Binary Tree
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        def process(root, path):
            if root:
                path = str(root.val)
                if root.left is not None:
                    path = path + '(' + process(root.left, '') + ')'
                if root.left is None and root.right is not None:
                    path = path + '()'
                if root.right is not None:
                    path = path + '(' + process(root.right, '') + ')'
            return path

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ''
        
        stack = [t]
        record = set()
        path = ''
        while len(stack) > 0:
            curr = stack[-1]
            if curr in record: # when all sub-trees are processed, we need to add ')'
                stack.pop()
                path = path + ')'
            else:
                record.add(curr)
                path = path + '(' + str(curr.val)
                if curr.right is not None:
                    stack.append(curr.right)
                if curr.left is not None:
                    stack.append(curr.left)
                if curr.left is None and curr.right is not None:
                    path = path +'()'
        return path[1:-1]

# 617. Merge Two Binary Trees
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        elif t1 is None and t2 is not None:
            return t2
        elif t2 is None and t1 is not None:
            return t1
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self. mergeTrees(t1.right, t2.right)
        return t1

# 624. Maximum Distance in Arrays
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = -1
        minval = arrays[0][0]
        maxval = arrays[0][-1]
        
        for nums in arrays[1:]:
            res = max(res, abs(nums[0]-maxval), abs(nums[-1]-minval))
            minval = min(minval, nums[0])
            maxval = max(maxval, nums[-1])
        return res

# 628. Maximum Product of Three Numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = sorted(nums)
        return max(n[0]*n[1]*n[-1], n[-1]*n[-2]*n[-3])

class Solution: # similar as sorting the array, but what we want are only the 2 smallest values and the 3 largest values
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = float(inf)
        min2 = float(inf)
        max1 = float(-inf)
        max2 = float(-inf)
        max3 = float(-inf)
        for n in nums:
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
            
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
        return max(min1*min2*max1, max1*max2*max3)

# 633. Sum of Square Numbers
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c in [0,1,2]:
            return True
        else:
            n = int(sqrt(c))
            while n >= int(sqrt(c//2)):
                remain = c - n**2
                if int(sqrt(remain)) ** 2 == remain:
                    return True
                n = n-1
            return False

# 637. Average of Levels in Binary Tree
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        while len(queue) > 0:
            num_trees = len(queue)
            level_total = 0
            for i in range(num_trees):
                curr = queue.pop(0)
                level_total += curr.val
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            res.append(level_total/num_trees)
        return res

# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        else:
            total = sum(nums[:k])
            best = total/k
            start = nums[0]
            end = nums[k-1]
            for i in range(k,len(nums)):
                end = nums[i]
                total = total-start+end
                start = nums[i-k+1]
                best = max(best, total/k)
            return best

# 645. Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = set(nums)
        n = len(nums)
        return [sum(nums)-sum(a), n*(n+1)//2-sum(a)]

# 653. Two Sum IV - Input is a BST
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        
        stack = [root]
        res = set()
        while len(stack) > 0:
            curr = stack.pop()
            if k - curr.val not in res:
                res.add(curr.val)
            else:
                return True
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return False

# 657. Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n = len(moves)
        if n == 0:
            return True
        elif n % 2 == 1:
            return False
        else:
            store = {'R':0, 'L':0, 'U':0, 'D':0}
            for s in moves:
                store[s] +=1
            if store['R'] == store['L'] and store['U'] == store['D']:
                return True
            else:
                return False

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = moves.count('R')
        l = moves.count('L')
        u = moves.count('U')
        d = moves.count('D')
        return r==l and u==d

# 661. Image Smoother
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        l = len(M)
        w = len(M[0])
        res = []
        for i in range(l):
            res.append([0]*w)
        for i in range(l):
            for j in range(w):
                total = 0
                count = 0
                for subl in (i-1, i, i+1):
                    for subw in (j-1, j, j+1):
                        if 0<=subl<=l-1 and 0<=subw<=w-1:
                            count += 1
                            total += M[subl][subw]
                res[i][j] = total // count
        return res

# 665. Non-decreasing Array
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return True
        else:
            problem = None
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    if problem is not None:
                        return False
                    problem = i
            
            return problem is None or problem == 0 or problem == len(nums)-2 or nums[problem-1]<=nums[problem+1] or nums[problem]<=nums[problem+2]

# 669. Trim a Binary Search Tree
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        while root is not None and (root.val > R or root.val < L):
            if root.val > R:
                root = root.left
            else:
                root = root.right
        
        if root is None:
            return None
        
        if root.left is not None:
            root.left = self.trimBST(root.left, L, R)
        if root.right is not None:
            root.right = self.trimBST(root.right, L, R)
        return root

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def process(root):
            if root is None:
                return None
            elif root.val > R:
                return process(root.left)
            elif root.val < L:
                return process(root.right)
            else:
                root.left = process(root.left)
                root.right = process(root.right)
                return root
        
        return process(root)

# 671. Second Minimum Node In a Binary Tree
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        elif root.left is None and root.right is None:
            return -1
        else:
            val = root.val
            queue = [root.left, root.right]
            res = val
            while len(queue) > 0:
                n_trees = len(queue)
                for i in range(n_trees):
                    curr = queue.pop(0)
                    if curr.val != val:
                        if res == val:
                            res = curr.val
                        else:
                            res = min(res, curr.val)
                    if curr.left is not None:
                        queue.append(curr.left)
                        queue.append(curr.right)
            return res if res != val else -1

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = float(inf)
        min1 = root.val
        
        def process(root):
            if root:
                if min1 < root.val < self.ans:
                    self.ans = root.val
                elif root.val == min1: # if root.val > min1, no need to search the subtree of this root because root.val is the smallest one except min1 in this tree
                    process(root.left)
                    process(root.right)
        process(root)
        return self.ans if self.ans < float(inf) else -1

# 674. Longest Continuous Increasing Subsequence
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        else:
            count = 1
            res = 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    count += 1
                else:
                    res = max(res, count)
                    count = 1
            return max(res, count)

# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        if len(s) == 0 or len(s) == 1:
            return True
        else:
            l = 0
            r = len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
            return True

# 682. Baseball Game
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for s in ops:
            if s == 'C':
                if stack != []:
                    stack.pop()
            elif s == 'D':
                if stack != []:
                    stack.append(stack[-1]*2)
            elif s == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(s))
        return sum(stack)

# 686. Repeated String Match
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B == '':
            return 1
        else:
            n = (len(B)-1) // len(A) + 1
            if B in A*(n):
                return n
            if B in A*(n+1):
                return n+1
        return -1