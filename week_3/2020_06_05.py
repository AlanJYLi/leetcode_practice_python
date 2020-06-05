# 538. Convert BST to Greater Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # recursion
    def __init__(self):
        self.total = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

class Solution: # iteration
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        stack = []
        total = 0
        curr = root
        while len(stack) > 0 or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.right
            
            curr = stack.pop()
            total += curr.val
            curr.val = total
            
            curr = curr.left
        
        return root

# 541. Reverse String II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        
        chunk = len(s) // (2*k)
        remain = len(s) % (2*k)
        new = ''
        for i in range(chunk):
            new = new + s[(i*(2*k)):(i*(2*k)+k)][::-1] + s[(i*(2*k)+k):(i*(2*k)+2*k)]
        if remain == 0:
            return new
        elif remain > 0 and remain <= k:
            new = new + s[len(s)-remain:][::-1]
            return new
        else:
            new = new + s[len(s)-remain:len(s)-remain+k][::-1] + s[len(s)-remain+k:]
            return new

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)

# 543. Diameter of Binary Tree
class Solution: # iteration: relatively slow in this problem
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def getDepth(root):
            if root is None:
                return 0
            return 1+max(getDepth(root.left),getDepth(root.right))
        
        def diameterPassRoot(root):
            if root is None:
                return 0
            return getDepth(root.left)+getDepth(root.right)
        
        d = 0
        if root is None:
            return 0
        
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            d = max(d, diameterPassRoot(curr))
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return d

class Solution: # recursion
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0
         
        def depth(root):
            if root is None:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            self.d = max(self.d, l+r)
            return max(l, r) + 1
        
        depth(root)
        return self.d

# 551. Student Attendance Record I
class Solution:
    def checkRecord(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        return s.count('A') <= 1 and s.count('LLL') == 0

# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split()
        news = ''
        for e in sl:
            news = news + ' ' + e[::-1]
        return news[1:]

#559. Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            return 1+max([self.maxDepth(c) for c in root.children])

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        depth = 0
        while len(stack) > 0:
            curr, curr_d = stack.pop()
            if curr is not None:
                depth = max(depth, curr_d)
                for c in curr.children:
                    stack.append((c, curr_d+1))
        return depth

# 561. Array Partition I
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        a = sorted(nums)
        total = 0
        for i in range(0,len(a),2):
            total += a[i]
        return total

# 563. Binary Tree Tilt
def traverse(root):
            res = []
            if root:
                res = traverse(root.left)
                res = res + traverse(root.right)
                if root.left is None and root.right is None:
                    res.append(0)
                elif root.left is None and root.right is not None:
                    res.append(abs(root.right.val))
                    root.val += root.right.val
                elif root.left is not None and root.right is None:
                    res.append(abs(root.left.val))
                    root.val += root.left.val
                else:
                    res.append(abs(root.left.val-root.right.val))
                    root.val += root.right.val + root.left.val
            return res
        
        res = traverse(root)
        return sum(res)

class Solution: # more clean one
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        
        def traverse(root):
            if root is None:
                return 0
            
            l = traverse(root.left)
            r = traverse(root.right)
            self.tilt += abs(l-r)         
            return l+r+root.val
        
        traverse(root)
        return self.tilt

# 566. Reshape the Matrix
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if nums == []:
            return nums
        
        r0 = len(nums)
        c0 = len(nums[0])
        if r0*c0 != r*c or (r0 == r and c0 == c):
            return nums
        else:
            res = []
            for i in range(r):
                res.append([0]*c)
            # cannot assign res = [[0]*c]*r
            # each list in res points to the same one
            count = 0
            for i in range(r0):
                for j in range(c0):
                    num = nums[i][j]
                    count += 1
                    res[(count-1) // c][(count-1) % c] = num
            return res

# 572. Subtree of Another Tree
class Solution: # preorder traverse the tree, record the string of path, and check sub string
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def preorderPath(root):
            path = ''
            if root:
                path += '#'+str(root.val) # if no '#', [23] and [2,3] is the same in string
                if root.left is None:
                    path += 'null'
                path = path + preorderPath(root.left)
                if root.right is None:
                    path += 'null'
                path = path + preorderPath(root.right)
            return path
        
        spath = preorderPath(s)
        print(spath)
        tpath = preorderPath(t)
        print(tpath)
        return tpath in spath

# 575. Distribute Candies
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kind = len(set(candies))
        num = len(candies) // 2
        if kind <= num:
            return kind
        else:
            return num

# 581. Shortest Unsorted Continuous Subarray
class Solution: # brute force: slow
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        a = nums
        while len(a) > 0:
            if a[0] == min(a):
                a = a[1:]
            if len(a) > 0 and a[-1] == max(a):
                a = a[:-1]
            if len(a) > 0 and a[0] != min(a) and a[-1] != max(a):
                return len(a)
        return 0

class Solution: # compare original list with sorted list: faster
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        a = sorted(nums)
        start = len(nums)
        end = 0
        for i in range(len(nums)):
            if a[i] != nums[i]:
                start = i
                break
        for i in range(-1, -len(nums)-1, -1):
            if a[i] != nums[i]:
                end = len(nums) + i
                break
        return 0 if end<start else end-start+1

# 589. N-ary Tree Preorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution: # recursion
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root:
            res.append(root.val)
            if root.children != []:
                for c in root.children:
                    res = res + self.preorder(c)
        return res

class Solution: # iteration
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.children != []:
                for c in curr.children[::-1]:
                    stack.append(c)
        return res

# 590. N-ary Tree Postorder Traversal
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root:
            if root.children != []:
                for c in root.children:
                    res = res + self.postorder(c)
            res.append(root.val)
        return res

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.children != []:
                for c in curr.children:
                    stack.append(c)
        return res[::-1]

# 594. Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            store[num] = 1 if num not in store else store[num]+1
        res = 0
        for num in store:
            if num+1 in store:
                res = max(res, store[num]+store[num+1])
        return res

# 598. Range Addition II
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []: # edge case!
            return m*n
        amin = float(inf)
        bmin = float(inf)
        for op in ops:
            amin = min(amin, op[0])
            bmin = min(bmin, op[1])
        return amin*bmin
