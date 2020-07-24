# 1243. Array Transformation
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            prev = arr[0]
            count = 0
            for i in range(1, len(arr)-1):
                if arr[i] > prev and arr[i] > arr[i+1]:
                    prev = arr[i]
                    arr[i] -= 1
                elif arr[i] < prev and arr[i] < arr[i+1]:
                    prev = arr[i]
                    arr[i] += 1
                else:
                    prev = arr[i]
                    count += 1
            if count == len(arr)-2:
                return arr

# 1260. Shift 2D Grid
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)
        for _ in range(k):
            res = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m-1 and j == n-1:
                        res[0][0] = grid[i][j]
                    elif i < m-1 and j == n-1:
                        res[i+1][0] = grid[i][j]
                    else:
                        res[i][j+1] = grid[i][j]
            grid = res
        return grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)
        if k == 0:
            return grid
        else:
            res = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    newj = (j+k) % n
                    i_move = (j+k) // n
                    newi = (i+i_move) % m
                    res[newi][newj] = grid[i][j]
            return res

# 1266. Minimum Time Visiting All Points
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        res = 0
        for i in range(1,len(points)):
            p = points[i]
            q = points[i-1]
            res += max(abs(p[0]-q[0]), abs(p[1]-q[1]))
        return res

# 1275. Find Winner on a Tic Tac Toe Game
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return 'Pending'
        else:
            a = [moves[i] for i in range(0, len(moves),2)]
            b = [moves[i] for i in range(1, len(moves),2)]
            if len(a) > len(b):
                row_count = [0, 0, 0]
                col_count = [0, 0, 0]
                digleft_count = 0
                digright_count = 0
                for x, y in a:
                    row_count[x] += 1
                    col_count[y] += 1
                    if x == y:
                        digleft_count += 1
                    if (x == 1 and y == 1) or (abs(x-y) == 2):
                        digright_count += 1
                if max([max(row_count), max(col_count), digleft_count, digright_count]) == 3:
                    return 'A'
                if len(a) == 5:
                    return 'Draw'
            else:
                row_count = [0, 0, 0]
                col_count = [0, 0, 0]
                digleft_count = 0
                digright_count = 0
                for x, y in b:
                    row_count[x] += 1
                    col_count[y] += 1
                    if x == y:
                        digleft_count += 1
                    if (x == 1 and y == 1) or (abs(x-y) == 2):
                        digright_count += 1
                if max([max(row_count), max(col_count), digleft_count, digright_count]) == 3:
                    return 'B'
            return 'Pending'

# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for d in str(n):
            v = int(d)
            p *= v
            s += v
        return p-s
