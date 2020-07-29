# 1351. Count Negative Numbers in a Sorted Matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        count = 0
        i = 0
        j = c-1
        while i < r:
            while j >= 0 and grid[i][j] < 0:
                count += (r-i)
                j -= 1
            i += 1
        return count

# 1356. Sort Integers by The Number of 1 Bits
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        store = {}
        maxbit = 0
        for num in arr:
            bit = bin(num)[2:].count('1')
            if bit not in store:
                store[bit] = [num]
            else:
                store[bit].append(num)
            maxbit = max(maxbit, bit)
        res = []
        for i in range(maxbit+1):
            if i in store:
                res = res + sorted(store[i])
        return res

# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        store = {}
        new = sorted(nums)
        for i in range(len(new)):
            if i == 0:
                store[new[i]] = 0
            else:
                if new[i] > new[i-1]:
                    store[new[i]] = i
        return [store[n] for n in nums]

# 1380. Lucky Numbers in a Matrix
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min_pos = []
        for i in range(len(matrix)):
            row_min_col = 0
            row_min = matrix[i][row_min_col]
            for j in range(1, len(matrix[0])):
                if matrix[i][j] < row_min:
                    row_min_col = j
                    row_min = matrix[i][row_min_col]
            row_min_pos.append((i, row_min_col))
        res = []
        for i,j in row_min_pos:
            val = matrix[i][j]
            if all(val >= matrix[k][j] for k in range(len(matrix))):
                   res.append(val)
        return res

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = {min(r) for r in matrix}
        maxcol = {max(c) for c in zip(*matrix)} # zip(*) transpose the matrix
        return list(minrow & maxcol)

# 1394. Find Lucky Integer in an Array
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for n in set(arr):
            if n == arr.count(n):
                res = max(res, n)
        return res

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        store = {}
        for n in arr:
            store[n] = 1 if n not in store else store[n]+1
        
        res = -1
        for num, freq in store.items():
            if num == freq:
                res = max(res, num)
        return res
