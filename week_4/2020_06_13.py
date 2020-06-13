# 949. Largest Time for Given Digits
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        import itertools
        best = -1
        for i in itertools.permutations(A):
            time_num = 1000*i[0]+100*i[1]+10*i[2]+i[3]
            if (i[0]==2 and i[1]<4 or i[0]<=1) and i[2]<=5:
                best = max(best, time_num)
        if best == -1:
            return ''
        else:
            time = str(best)
            time = '0'*(4-len(time)) + time
            return time[:2]+':'+time[2:]

# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        store = {}
        for i, l in enumerate(order):
            store[l] = i
        
        def compare(a,b):
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    if store[a[i]] < store[b[j]]:
                        return True
                    else:
                        return False
            return i == len(a) and j <= len(b)
        
        for i in range(1,len(words)):
            if compare(words[i-1], words[i]):
                continue
            else:
                return False
        return True

# 961. N-Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        store = set()
        for n in A:
            if n in store:
                return n
            else:
                store.add(n)

# 965. Univalued Binary Tree
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        c = root.val
        while len(stack) > 0:
            curr = stack.pop()
            if curr.val != c:
                return False
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return True

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.res = True
        
        def process(root):
            if root:
                c = root.val
                if root.left is not None:
                    if root.left.val == c:
                        process(root.left)
                    else:
                        self.res = False
                if root.right is not None:
                    if root.right.val == c:
                        process(root.right)
                    else:
                        self.res = False
        
        process(root)
        return self.res

# 970. Powerful Integers
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        if bound == 0:
            return []
        
        limit = len(bin(bound).split('b')[-1])-1
        for i in range(limit+1):
            for j in range(limit+1):
                num = x**i+y**j
                if num <= bound:
                    res.add(num)
        return list(res)

# 976. Largest Perimeter Triangle
class Solution: # exceed time limit in Leetcode
    def largestPerimeter(self, A: List[int]) -> int:
        
        def getPerimeter(a, b, c):
            if a+b>c and b+c>a and c+a>b:
                return a+b+c
            else:
                return 0
        
        best = 0
        import itertools
        for a, b, c in itertools.combinations(A,3):
            best = max(best, getPerimeter(a,b,c))
        return best

class Solution: # sort and search
    def largestPerimeter(self, A: List[int]) -> int:
        a = sorted(A, reverse=True)
        for i in range(2,len(a)):
            if a[i] + a[i-1] > a[i-2]:
                return a[i] + a[i-1] + a[i-2]
        return 0

# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])

class Solution: # linear search
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[0] >= 0:
            return [x**2 for x in A]
        elif A[-1] <= 0:
            return [A[i]**2 for i in range(-1, -len(A)-1,-1)]
        else:
            p = 0 # non-negative pointer
            while A[p] < 0:
                p += 1
            n = p-1 # negative pointer
            res = []
            while n >= 0 and p < len(A):
                if A[n]**2 < A[p]**2:
                    res.append(A[n]**2)
                    n -= 1
                else:
                    res.append(A[p]**2)
                    p += 1
            while n >= 0:
                res.append(A[n]**2)
                n -= 1
            while p < len(A):
                res.append(A[p]**2)
                p += 1
            return res

# 985. Sum of Even Numbers After Queries
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        curr = sum([x for x in A if x%2==0])
        res = []
        for val, index in queries:
            if A[index]%2 == 1 and val%2 == 1:
                curr += A[index]+val
            elif A[index]%2 == 0 and val%2 == 1:
                curr -= A[index]
            elif A[index]%2 == 1 and val%2 == 0:
                pass
            else:
                curr += val
            A[index] = A[index]+val
            res.append(curr)
        return res

# 989. Add to Array-Form of Integer
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num = 0
        N = len(A)
        for i, d in enumerate(A):
            num += d*10**(N-i-1)
        num += K
        return map(int, str(num))

# 993. Cousins in Binary Tree
class Solution: #bfs
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root, 0, None)]
        store = {}
        while len(queue) > 0:
            curr, depth, parent = queue.pop(0)
            store[curr.val] = (depth, parent)
            if x in store and y in store:
                break
            if curr.left is not None:
                queue.append((curr.left, depth+1, curr))
            if curr.right is not None:
                queue.append((curr.right, depth+1, curr))
        return store[x][0] == store[y][0] and store[x][1] != store[y][1]

# 997. Find the Town Judge
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and trust == []:
            return 1
        
        be_trusted = {}
        trust_other = set()
        for person, target in trust:
            trust_other.add(person)
            be_trusted[target] = 1 if target not in be_trusted else be_trusted[target]+1
        if len(trust_other) == N:
            return -1
        else:
            for p in be_trusted:
                if be_trusted[p] == N-1 and p not in trust_other:
                    return p
            return -1

class Solution: # similar approach
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        
        indegree = [0]*(N+1)
        outdegree = [0]*(N+1)
        
        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1
        
        for i in range(1, N+1):
            if indegree[i] == N-1 and outdegree[i] == 0:
                return i
        return -1