# 45. Jump Game II
class Solution: # exceed time limit
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        if target <= 1:
            return target
        else:
            store = {}
            start = nums[0]
            for i in range(1, start+1):
                store[i] = [1]
            for j in range(1,len(nums)-1):
                step = nums[j]
                for k in range(j+1, j+step+1):
                    if k in store:
                        temp = [x+1 for x in store[k]]
                        store[k] = store[k]+temp
                    else:
                        temp = [x+1 for x in store[j]]
                        store[k] = temp[:]
                    if target in store:
                        return min(store[target])
            return min(store[target])

class Solution: # greedy approach
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        if target <= 1:
            return target
        
        max_coverage = 0
        jump_start_index = 0
        count = 0
        for i in range(len(nums)):
            step = nums[i]
            max_coverage = max(max_coverage, i+step)
            if jump_start_index == i:
                jump_start_index = max_coverage
                count += 1
                if max_coverage >= target:
                    return count
        return count

# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def insertone(a, val):
            res = []
            for i in range(len(a)+1):
                temp = a[:i] + [val] + a[i:]
                res.append(temp)
            return res
                
        
        def process(nums):
            if len(nums) == 1:
                return [nums]
            elif len(nums) == 2:
                return [[nums[0], nums[1]], [nums[1],nums[0]]]
            else:
                res = []
                temp = nums[0]
                prev = process(nums[1:])
                for a in prev:
                    res = res + insertone(a, temp)
                return res
            
        return process(nums)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=0):
            if first == len(nums):
                res.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        res = []
        backtrack(0)
        return res

# 47. Permutations II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def insertone(a, val):
            res = []
            for i in range(len(a)+1):
                if i == len(a):
                    temp = a + [val]
                    res.append(temp)
                elif val == a[i]:
                    continue
                else:
                    temp = a[:i] + [val] + a[i:]
                    res.append(temp)
            return res
        
        def process(nums):
            if len(nums) == 1:
                return [nums]
            elif len(nums) == 2:
                return insertone([nums[0]], nums[1])
            else:
                res = []
                temp = nums[0]
                prev = process(nums[1:])
                for a in prev:
                    res = res + insertone(a, temp)
                return res
        
        res = [x for x in map(tuple, process(nums))]
        res = set(res)
        return [ x for x in map(list, res)]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=0):
            if first == len(nums):
                res.append(nums[:])
            else:
                used = set()
                for i in range(first, len(nums)):
                    if nums[i] in used:
                        continue
                    else:
                        used.add(nums[i])
                        nums[first], nums[i] = nums[i], nums[first]
                        backtrack(first+1)
                        nums[first], nums[i] = nums[i], nums[first]
        
        res = []
        backtrack(0)
        return res

# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        circle = (n-1)//2+1
        for i in range(circle):
            for j in range(i,n-1-i):
                start = {(i, j)}
                curr = matrix[i][j]
                rotate = (j, n-1-i)
                while rotate not in start:
                    temp = matrix[rotate[0]][rotate[1]]
                    matrix[rotate[0]][rotate[1]] = curr
                    curr = temp
                    rotate = (rotate[1], n-1-rotate[0])
                matrix[rotate[0]][rotate[1]] = curr

class Solution: # transpose and then reverse each row
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse the row
        for i in range(n):
            matrix[i].reverse()

# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            unique = ''.join(sorted(s))
            if unique not in store:
                store[unique] = [s]
            else:
                store[unique].append(s)
        return list(store.values())

class Solution: # the count of each letter is the unique mark of anagrams. Better than sort in time complexity 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getcount(s):
            count = [0] * 26
            for l in s:
                count[ord(l)-ord('a')] += 1
            return tuple(count)
        
        store = {}
        for s in strs:
            unique = getcount(s)
            if unique not in store:
                store[unique] = [s]
            else:
                store[unique].append(s)
        return list(store.values())

# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return 0
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        
        if x < 0 and n%2 == 1:
            sign = -1
        else:
            sign = 1
        if n > 0:
            inverse = False
        else:
            inverse = True 
        
        x = abs(x) # similar approach as Q29. Divide Two Integers
        if n > 0:
            n = -n # n in range (-2^31, 2^31-1), so change n to negative can avoid overflow
        HALF_MIN_INT = -1073741824
        store = {0:1, -1:x, -2:x*x}
        res = 1
        while n < -1:
            power = -2
            while power >= HALF_MIN_INT and power*2 >= n:
                store[power*2] = store[power]*store[power]
                power = power*2
            res = res*store[power]
            n = n-power
        res = res*store[n]*sign
        return res if inverse==False else 1/res

# 51. N-Queens
class Solution: # generate permutations of list[1,2,...,n], and check if it's valid
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def valid(a): # check the permutation is valid or not
            for i in range(len(a)):
                for j in range(0,i):
                    if abs(a[i]-a[j]) == i-j:
                        return False
                for j in range(i+1,len(a)):
                    if abs(a[i]-a[j]) == j-i:
                        return False
            return True
        
        def toresult(a):
            res = []
            n = len(a)
            for num in a:
                s = ['.']*n
                s[num-1] = 'Q'
                res.append(''.join(s))
            return res
                
        
        def backtrack(first=0):
            if first == len(nums):
                if valid(nums[:]):
                    res.append(toresult(nums[:]))
            else:
                for i in range(first, len(nums)):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first+1)
                    nums[first], nums[i] = nums[i], nums[first]
        
        if n == 1:
            return [['Q']]
        nums = [x for x in range(1,n+1)]
        res = []
        backtrack()
        return res

class Solution: # similar to Q37. Sudoku Solver
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = [0] * n
        left_to_right = [0] * (2*n-1) # diagonal
        right_to_left = [0] * (2*n-1) # diagonal
        record = set()
        res = []
        
        def can_place(r, c): # a quicker way to check validity
            return cols[c] + left_to_right[r-c] + right_to_left[r+c] == 0
        
        def place_one(r, c):
            record.add((r,c))
            cols[c] = 1
            left_to_right[r-c] = 1
            right_to_left[r+c] = 1
        
        def remove_one(r, c):
            record.remove((r,c))
            cols[c] = 0
            left_to_right[r-c] = 0
            right_to_left[r+c] = 0
        
        def to_solution():
            s = []
            for r,c in sorted(record):
                s.append('.'*c+'Q'+'.'*(n-1-c))
            res.append(s)
        
        def backtrack(r=0):
            for c in range(n):
                if can_place(r, c):
                    place_one(r, c)
                    if r == n-1:
                        to_solution()
                    else:
                        backtrack(r+1)
                    remove_one(r, c)
        
        backtrack()
        return res

# 52. N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [0] * n
        left_to_right = [0] * (2*n-1)
        right_to_left = [0] * (2*n-1)
        
        def can_place(r, c):
            return cols[c]+left_to_right[r-c]+right_to_left[r+c] == 0
        
        def place_one(r, c):
            cols[c] = 1
            left_to_right[r-c] = 1
            right_to_left[r+c] = 1
        
        def remove_one(r, c):
            cols[c] = 0
            left_to_right[r-c] = 0
            right_to_left[r+c] = 0
        
        def backtrack(r=0):
            for c in range(n):
                if can_place(r, c):
                    place_one(r, c)
                    if r == n-1:
                        self.count += 1
                    else:
                        backtrack(r+1)
                    remove_one(r, c)
        
        self.count = 0
        backtrack()
        return self.count

# 54. Spiral Matrix
class Solution: # learn from 48. Rotate Image, use reverse and transpose
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        if len(matrix) == 0:
            return res
        
        while len(matrix) > 1:
            res += matrix[0]
            matrix = matrix[1:]
            if len(matrix[0]) > 1: # reverse
                for i in range(len(matrix)):
                    matrix[i].reverse()
            if len(matrix) > 1: # transpose
                m = len(matrix)
                n = len(matrix[0])
                new = [[0]*m for i in range(n)]
                for i in range(m):
                    for j in range(n):
                        new[j][i] = matrix[i][j]
                matrix = new
            else:
                break
        return res+matrix[0]

class Solution: # traverse from outer layer to inner layer
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def layerorder(r1, c1, r2, c2):
            res = []
            for c in range(c1, c2+1):
                res.append(matrix[r1][c])
            for r in range(r1+1, r2+1):
                res.append(matrix[r][c2])
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1-1, -1):
                    res.append(matrix[r2][c])
                for r in range(r2-1, r1, -1):
                    res.append(matrix[r][c1])
            return res
        
        if matrix == []:
            return []
        
        res = []
        r1 = 0
        r2 = len(matrix)-1
        c1 = 0
        c2 = len(matrix[0])-1
        while c1<=c2 and r1<=r2:
            res += layerorder(r1, c1, r2, c2)
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res

# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums)-1):
            if i > res:
                return False
            res = max(res, i+nums[i])
            if res >= len(nums)-1:
                return True
        return False or len(nums) == 1

#56. Merge Intervals
class Solution: # divide and conqure
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals, key=lambda x: (x[0],x[1]))
        
        def mergeTwo(a,b):
            if a[1] < b[0]:
                return [a, b]
            else:
                return [[a[0], max(a[1],b[1])]]
        
        if len(s) == 0:
            return []
        elif len(s) == 1:
            return s
        else:
            while len(s) >= 2:
                res = []
                for i in range(0, len(s), 2):
                    if i < len(s)-1:
                        res += mergeTwo(s[i], s[i+1])
                    else:
                        res.append(s[i])
                if res == s:
                    temp = [res[0]]
                    for i in range(1,len(res), 2):
                        if i < len(res)-1:
                            temp += mergeTwo(res[i], res[i+1])
                        else:
                            temp.append(res[i])
                    res = temp
                if res == s:
                    break
                else:
                    s = res
            return res

class Solution: # merge directly
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals, key=lambda x: (x[0],x[1]))
        
        res = []
        for i in s:
            if res == [] or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1],i[1])
        return res

# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        s = sorted(intervals, key=lambda x: (x[0],x[1]))
        lo = newInterval[0]
        hi = newInterval[1]
        i = 0
        res = []
        while i < len(s):
            if hi < s[i][0]:
                res.append([lo, hi])
                res += s[i:]
                break
            elif lo > s[i][1]:
                res.append(s[i])
                if i == len(s)-1:
                    res.append([lo,hi])
                    break
                i += 1
            else:
                temp = [s[i]]
                j = i+1
                while j < len(s) and hi >= s[j][0] and lo <= s[j][1]:
                    temp.append(s[j])
                    j += 1
                merge = [min(lo, temp[0][0]), max(hi, temp[-1][1])]
                res.append(merge)
                if j == len(s):
                    break
                else:
                    while j < len(s):
                        res.append(s[j])
                        j += 1
                    break
        return res

# 59. Spiral Matrix II
class Solution: # Q54. Spiral Matrix
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0]*n for i in range(n)]
        self.record = 1
        
        def layerorder(r1, c1, r2, c2, record):
            for c in range(c1, c2+1):
                res[r1][c] = self.record
                self.record += 1
            for r in range(r1+1, r2+1):
                res[r][c2] = self.record
                self.record += 1
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1-1, -1):
                    res[r2][c] = self.record
                    self.record += 1
                for r in range(r2-1, r1, -1):
                    res[r][c1] = self.record
                    self.record += 1
            
        r1 = 0
        r2 = n-1
        c1 = 0
        c2 = n-1
        while c1<=c2 and r1<=r2:
            layerorder(r1, c1, r2, c2, self.record)
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res