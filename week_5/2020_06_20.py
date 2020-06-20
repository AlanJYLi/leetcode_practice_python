# 60. Permutation Sequence
class Solution: # similar as n base system; represent by Factorial Number System 
    def getPermutation(self, n: int, k: int) -> str:
        if k == 1:
            return ''.join([str(x+1) for x in range(n)])
        elif k == 2:
            return ''.join([str(x+1) for x in range(n-2)])+str(n)+str(n-1)
        
        store = {-1:1, 0:1, 1:1, 2:2}
        for i in range(3, n+1):
            store[i] =store[i-1]*i
            if store[i] == k:
                return ''.join([str(x+1) for x in range(n-i)])+''.join([str(x) for x in range(n,n-i,-1)])
            elif store[i] > k:
                break
        order = i-1
        lo = store[order]
        res = ''.join([str(x+1) for x in range(n-i)])
        remain = [x+1 for x in range(n-i, n)]
        while len(remain) > 0:
            select = (k-1)//lo
            res += str(remain.pop(select))
            k = k - select*lo
            order -= 1
            lo = store[order]
        return res

# 61. Rotate List
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        def getlength(head):
            curr = head
            count = 0
            while curr is not None:
                count += 1
                curr = curr.next
            return count
        
        if head is None:
            return head
        
        l = getlength(head)
        step = l - k%l
        if step == l:
            return head
        
        prev = ListNode(0, head)
        curr = head
        while step > 0:
            curr = curr.next
            prev = prev.next
            step -= 1
        prev.next = None
        temp = curr
        while temp.next is not None:
            temp = temp.next
        temp.next = head
        return curr

class Solution: # more clear way: link the end to start to form a ring, then find new head and close the new tail
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        if head is None:
            return head
        
        curr = head
        count = 1
        while curr.next is not None:
            count += 1
            curr = curr.next
        curr.next = head
        
        tail = head
        step = count - k % count - 1
        while step > 0:
            tail = tail.next
            step -= 1
        res = tail.next
        tail.next = None
        return res

# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mark = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    mark[i][j] = 1
                elif i == 0 and j > 0:
                    mark[i][j] = 1
                elif i > 0 and j == 0:
                    mark[i][j] = 1
                else:
                    mark[i][j] = mark[i-1][j] + mark[i][j-1]
        return mark[n-1][m-1]

# 63. Unique Paths II 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mark = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    mark[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        mark[i][j] = 1
                    elif i == 0 and j > 0:
                        mark[i][j] = mark[i][j-1]
                    elif i > 0 and j == 0:
                        mark[i][j] = mark[i-1][j]
                    else:
                        mark[i][j] = mark[i-1][j] + mark[i][j-1]
        return mark[m-1][n-1]

# 64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mark = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    mark[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    mark[i][j] = grid[i][j] + mark[i][j-1]
                elif i > 0 and j == 0:
                    mark[i][j] = grid[i][j] + mark[i-1][j]
                else:
                    mark[i][j] = grid[i][j] + min(mark[i-1][j], mark[i][j-1])
        return mark[m-1][n-1]

# 65. Valid Number
class Solution:
    def isNumber(self, s: str) -> bool:
        def int_valid(s):
            if s == '' or s == '+' or s == '-':
                return False
            for i in range(len(s)):
                if s[i].isdigit() == False and i != 0:
                    return False
                elif s[i].isdigit() == False and i==0 and s[i] not in {'-','+'}:
                    return False
            return True
        
        s = s.strip()
        dot = False
        for i in range(len(s)):
            if s[i].isalpha() and s[i] != 'e':
                return False
            elif s[i] in {'+', '-'} :
                if i != 0:
                    return False
                elif i == 0 and len(s) == 1:
                    return False
                elif i==0 and i+1<len(s) and s[i+1] == 'e':
                    return False
                elif i==0 and len(s)==2 and s[1]=='.':
                    return False
            elif s[i] == 'e':
                if i == 0:
                    return False
                else:
                    return int_valid(s[i+1:])
            elif s[i] == '.':
                if dot == True:
                    return False
                else:
                    if i == 0 and len(s) == 1:
                        return False
                    elif i == 0 and s[i+1].isdigit() == False:
                        return False
                    elif 0 < i < len(s)-1 and not (s[i+1].isdigit() or s[i-1].isdigit()):
                        return False
                    else:
                        dot = True
            elif s[i] == ' ':
                return False
        return True and s != ''

class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        a = '^(([+-]?[0-9]+)(\.[0-9]+)?|([+-]?\.[0-9]+)|([+-]?[0-9]+\.))(e[+-]?[0-9]+)?$'
        # ([+-]?[0-9]+)(\.[0-9]+)?： normal numbers
        # ([+-]?\.[0-9]+): .28137
        # ([+-]?[0-9]+\.): 2913.
        return re.match(a, s.strip()) is not None

# 68. Text Justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        temp = []
        length = 0
        count = 0
        i = 0
        while i < len(words):
            w = words[i]
            if len(w)+length+count < maxWidth:
                temp.append(w)
                length += len(w)
                count += 1
                i += 1
            elif len(w)+length+count == maxWidth:
                temp.append(w)
                res.append(' '.join(temp))
                temp = []
                length = 0
                count = 0
                i += 1
            else:
                space = maxWidth - length
                if count == 1:
                    line = temp[0] + ' '*space
                elif count == 2:
                    line = temp[0] + ' '*space + temp[1]
                else:
                    base = space // (count-1)
                    remain = space % (count-1)
                    line = temp[0]
                    for j in range(1,len(temp)):
                        if j <= remain:
                            line += ' '*(base+1) + temp[j]
                        else:
                            line += ' '*base + temp[j]
                res.append(line)
                temp = []
                length = 0
                count = 0
        if temp != []:
            line = ' '.join(temp) + ' '*(maxWidth - length - count + 1)
            res.append(line)
        return res

# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        element = path.split('/')
        stack = []
        for i in range(len(element)-1, -1, -1):
            e = element[i]
            if e != '':
                if e == '..':
                    stack.append(e)
                elif e == '.':
                    continue
                else:
                    if len(stack) > 0 and stack[-1] == '..':
                        stack.pop()
                    else:
                        stack.append(e)
        res = '/'
        while len(stack) > 0:
            e = stack.pop()
            if e != '..':
                res += e + '/'
        
        return res[:len(res)-1] if len(res) > 1 else res

# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0 or n == 0:
            return max(m,n)
        mark = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            mark[i][0] = i
        for i in range(n+1):
            mark[0][i] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                left = mark[i-1][j]
                up = mark[i][j-1]
                diag = mark[i-1][j-1]
                if word1[i-1] == word2[j-1]:
                    mark[i][j] = min(left+1, up+1, diag)
                else:
                    mark[i][j] = min(left+1, up+1, diag+1)
        
        return mark[m][n]

# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

class Solution: # how to achieve constant space complexity: use the first row and column as mark
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
            
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
            
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
            
        if first_col:
            for i in range(m):
                matrix[i][0] = 0

