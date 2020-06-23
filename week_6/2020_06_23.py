# 85. Maximal Rectangle
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        mark = [[0]*len(matrix[0]) for i in range(len(matrix))]
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                else:
                    mark[i][j] = mark[i][j-1]+1 if j > 0 else 1
                    w = mark[i][j]
                
                for k in range(i,-1,-1):
                    w = min(w, mark[k][j])
                    res = max(res, w*(i-k+1))
        return res

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def histo(a): # Q84. Largest Rectangle in Histogram
            stack = [(-1,-1)]
            res = 0
            for i, val in enumerate(a):
                while stack[-1][0] != -1 and stack[-1][1] >= val:
                    index, num = stack.pop()
                    res = max(res, num*(i-stack[-1][0]-1))
                stack.append((i,val))
            
            while stack[-1][0] != -1:
                index, num = stack.pop()
                res = max(res, num*(len(a)-stack[-1][0]-1))
            return res
        
        if matrix == []:
            return 0
        
        res = 0
        hist = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hist[j] = hist[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, histo(hist))
        return res

# 86. Partition List
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        d1 = dummy1
        d2 = dummy2
        curr = head
        while curr is not None:
            if curr.val < x:
                d1.next = curr
                d1 = d1.next
            else:
                d2.next = curr
                d2 = d2.next
            curr = curr.next
        d2.next = curr
        d1.next = dummy2.next
        return dummy1.next

# 87. Scramble String
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        store = {}
        def process(s1,s2):
            if (s1,s2) in store:
                return store[(s1,s2)]
            else:
                if s1 == s2:
                    store[(s1,s2)] = True
                    return True
                if sorted(s1) != sorted(s2):
                    store[(s1,s2)] = False
                    return False
                for i in range(len(s1)-1, 0, -1):
                    if (process(s1[:i], s2[:i]) and process(s1[i:],s2[i:])) or (process(s1[:i], s2[-i:]) and process(s1[i:],s2[:-i])):
                        return True
                store[(s1,s2)] = False
                return False
        
        return process(s1,s2)

# 89. Gray Code
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [x^x>>1 for x in range(2**n)]

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0, 1]
        for i in range(1,n):
            for num in reversed(res):
                res.append(num+2**i)
        return res

# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            if tuple(curr[:]) not in seen:
                res.append(curr[:])
                seen.add(tuple(curr[:]))
            for i in range(first, len(nums)):
                num = nums[i]
                curr.append(num)
                backtrack(i+1, curr)
                curr.pop()
        nums.sort()
        res = []
        seen = set()
        backtrack()
        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            res.append(curr[:])
            for i in range(first, len(nums)):
                if nums[i] == nums[i-1] and i > first:
                    continue
                else:
                    curr.append(nums[i])
                    backtrack(i+1, curr)
                    curr.pop()
        
        nums.sort()
        res = []
        backtrack()
        return res

# 91. Decode Ways
class Solution:
    def numDecodings(self, s: str) -> int:
        # cannot start with zero
        if s == '' or s[0] == '0':
            return 0
        # consecutive zeros cannot exist
        # number before zero must be 1 or 2
        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1]==s[i]:
                return 0
            if s[i] == '0' and s[i-1] not in {'1','2'}:
                return 0
        
        dq = [(0,0)]*len(s) #(a,b):(number of ways, number of ways end with one digit)
        for i in range(len(s)):
            if i == 0:
                dq[i] = (1,1)
            else:
                if s[i] == '0':
                    dq[i] = (dq[i-1][0],0)
                else:
                    if 10<int(s[i-1]+s[i])<=26 and ((i+1<len(s) and s[i+1] != '0') or (i+1==len(s))):
                        dq[i] = (dq[i-1][1]*2+dq[i-1][0]-dq[i-1][1],dq[i-1][0])
                    elif i+1<len(s) and s[i+1] == '0':
                        dq[i] = (dq[i-1][0],0)
                    else:
                        dq[i] = (dq[i-1][0],dq[i-1][0])
        return dq[-1][0]

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0
        
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2,len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

# 92. Reverse Linked List II
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        d = dummy
        curr = head
        i = 1
        while i < m:
            d.next = curr
            d = d.next
            curr = curr.next
            i += 1
        stack = []
        while i <= n:
            stack.append(ListNode(curr.val))
            curr = curr.next
            i += 1
        while len(stack) > 0:
            d.next = stack.pop()
            d = d.next
        d.next = curr
        return dummy.next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None
        
        curr = head
        prev = None
        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1
            n -= 1
        
        tail = curr
        remain = prev
        
        while n > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1
        
        if remain is not None:
            remain.next = prev
        else:
            head = prev
        tail.next = curr
        return head

# 93. Restore IP Addresses
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(position=-1, dots=3):
            for curr in range(position+1, min(len(s)-1,position+4)):
                temp = s[position+1:curr+1]
                if (int(temp)<=255 and temp[0]!='0') or (len(temp)==1):
                    ip.append(temp)
                    if dots-1 == 0:
                        remain = s[curr+1:len(s)]
                        if (int(remain)<=255 and remain[0]!='0') or (len(remain)==1):
                            ip.append(remain)
                            res.append('.'.join(ip))
                            ip.pop()
                    else:
                        backtrack(curr, dots-1)
                    ip.pop()
        
        res = []
        ip = []
        backtrack()
        return res

# 94. Binary Tree Inorder Traversal
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res+inorder(root.right)
            return res
        
        return inorder(root)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        res = []
        stack = []
        curr = root
        while curr is not None or len(stack)>0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

# 95. Unique Binary Search Trees II
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def process(l,r):
            if l > r:
                return [None,]
            
            trees = []
            for i in range(l, r+1):
                left = process(l,i-1)
                right = process(i+1,r)
                
                for lt in left:
                    for rt in right:
                        curr = TreeNode(i)
                        curr.left = lt
                        curr.right = rt
                        trees.append(curr)
            return trees
        
        return process(1,n) if n>0 else []

# 96. Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]