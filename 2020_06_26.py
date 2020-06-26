# 126. Word Ladder II
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in set(wordList):
            return []
        
        store = {}
        l = len(beginWord)
        for w in wordList:
            for i in range(l):
                s = w[:i] + '*' + w[i+1:]
                if s in store:
                    store[s].append(w)
                else:
                    store[s] = [w]
        res = []
        queue = [(beginWord, [beginWord])]
        seen = set([beginWord])
        done = False
        while len(queue) > 0 and done == False:
            n = len(queue)
            check = set()
            for i in range(n):
                w, path = queue.pop(0)
                for j in range(l):
                    s = w[:j] + '*' + w[j+1:]
                    if s not in store:
                        continue
                    for changeto in store[s]:
                        if changeto == endWord:
                            res.append(path+[changeto])
                            done = True
                        if changeto not in seen:
                            check.add(changeto)
                            queue.append((changeto, path+[changeto]))
            for checked in check:
                seen.add(checked)
        return res

# 127. Word Ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0
        
        store = {}
        l = len(beginWord)
        for w in wordList:
            for i in range(l):
                s = w[:i] + '*' + w[i+1:]
                if s in store:
                    store[s].append(w)
                else:
                    store[s] = [w]
        
        queue = [(beginWord,1)]
        seen = set([beginWord])
        while len(queue) > 0:
            w, level = queue.pop(0)
            for j in range(l):
                s = w[:j] + '*' + w[j+1:]
                if s not in store:
                    continue
                for changeto in store[s]:
                    if changeto == endWord:
                        return level+1
                    if changeto not in seen:
                        seen.add(changeto)
                        queue.append((changeto, level+1))
        return 0

# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        res = 0
        nset = set(nums)
        for n in nset:
            if n-1 not in nset:
                curr = n
                l = 1
                
                while curr+1 in nset:
                    curr += 1
                    l += 1
                
                res = max(res,l)
        return res

# 129. Sum Root to Leaf Numbers
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def process(root, path):
            if root:
                path += str(root.val)
                if root.left is None and root.right is None:
                    self.res += int(path)
                process(root.left, path)
                process(root.right, path)
        
        process(root,'')
        return self.res

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        stack = [(root,0)]
        while len(stack) > 0:
            curr, n = stack.pop()
            if curr is not None:
                n = n*10+curr.val
                if curr.left is None and curr.right is None:
                    res += n
                else:
                    stack.append((curr.left, n))
                    stack.append((curr.right, n))
        return res

# 130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        
        R = len(board)
        C = len(board[0])
        def process(board,r,c):
            if board[r][c] != 'O':
                return
            board[r][c] = 'E'
            if c < C-1:
                process(board, r, c+1)
            if r < R-1:
                process(board, r+1, c)
            if c > 0:
                process(board, r, c-1)
            if r > 0:
                process(board, r-1, c)
        
        positions = []
        for i in range(R):
            for j in [0, C-1]:
                positions.append((i, j))
        for i in [0, R-1]:
            for j in range(C):
                positions.append((i,j))
        positions = set(positions)
        for r, c in positions:
            process(board,r,c)
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

# 131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []
        
        queue = [list(s)]
        res = []
        while len(queue) > 0:
            n = len(queue)
            for j in range(n):
                curr = queue.pop(0)
                res.append(tuple(curr))
                for i in range(len(curr)-1):
                    temp = None
                    if curr[i] == curr[i+1]:
                        temp = curr[:i] + [curr[i]+curr[i+1]] + curr[i+2:]
                    elif len(set(curr[i])) == 1 and set(curr[i]) == set(curr[i+1]):
                        temp = curr[:i] + [curr[i]+curr[i+1]] + curr[i+2:]
                    elif i > 0 and curr[i-1] == curr[i+1]:
                        temp = curr[:i-1] + [curr[i-1]+curr[i]+curr[i+1]] + curr[i+2:]
                    if temp is not None:
                        queue.append(temp)
                        res.append(tuple(temp))
        res = set(res)
        return [list(x) for x in res]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def backtrack(curr,s):
            if s == '':
                res.append(curr[:])
                return
            for i in range(1, len(s)+1):
                if check(s[:i]):
                    backtrack(curr+[s[:i]], s[i:])
        
        res = []
        backtrack([],s)
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        if len(s) == 0:
            return []
        
        store = {}  
        def process(s):
            if s in store:
                return store[s]
            
            temp = []
            for i in range(1, len(s)+1):
                if check(s[:i]):
                    if i == len(s):
                        temp.append([s[:i]])
                    else:
                        subs = process(s[i:])
                        for sub in subs:
                            temp.append([s[:i]] + sub)
            store[s] = temp
            return temp
        
        return process(s)

# 132. Palindrome Partitioning II
class Solution: # exceed time limit
    def minCut(self, s: str) -> int:
        def check(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        if len(s) == 0 or len(s) == 1:
            return 0
        
        store = {}
        def process(s):
            if s in store:
                return store[s]
            
            temp = []
            for i in range(1, len(s)+1):
                if check(s[:i]):
                    if i == len(s):
                        temp.append([s[:i]])
                    else:
                        subs = process(s[i:])
                        for sub in subs:
                            temp.append([s[:i]] + sub)
            store[s] = temp
            return temp
        
        res = process(s)
        return min([x for x in map(len, res)])-1

class Solution: # dp
    def minCut(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1 or s == s[::-1]:
            return 0
        
        for i in range(1,len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        
        mark = [x-1 for x in range(len(s)+1)]
        for i in range(len(s)):
            r = 0
            while i-r>=0 and i+r<=len(s)-1 and s[i-r]==s[i+r]:
                mark[i+r+1] = min(mark[i+r+1], mark[i-r]+1)
                r += 1
            
            r = 0
            while i-r>=0 and i+r+1<=len(s)-1 and s[i-r]==s[i+r+1]:
                mark[i+r+2] = min(mark[i+r+2], mark[i-r]+1)
                r += 1
        return mark[-1]
