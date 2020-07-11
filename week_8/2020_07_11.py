# 221. Maximal Square
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0 for j in range(c)] for i in range(r)]
        # dp[i][j] represent the side length of the square in which position [i][j] is the bottom-right corner
        res = 0
        for i in range(r):
            for j in range(c):
                if i == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                elif j == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    dp[i][j] = min([dp[i][j-1], dp[i-1][j],dp[i-1][j-1]])+1 if matrix[i][j] == '1' else 0
                res = max(res, dp[i][j]**2)
        return res

# 253. Meeting Rooms II
class Solution: # exceed time limit
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0 or len(intervals[0]) == 0:
            return 0
        
        dp = []
        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if i == 0:
                dp = dp + [0]*e
                for j in range(s,e):
                    dp[j] = 1
            else:
                if e < len(dp):
                    for j in range(s,e):
                        dp[j] += 1
                else:
                    dp = dp + [0]*(e-len(dp)+1)
                    for j in range(s,e):
                        dp[j] += 1
        return max(dp)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0 or len(intervals[0]) == 0:
            return 0
        
        intervals.sort(key=lambda x: (x[0],x[1]))
        
        dp = []
        res = 0
        for i in intervals:
            if len(dp) == 0:
                dp.append(i[1])
            else:
                finish = min(dp)
                if i[0] < finish:
                    dp.append(i[1])
                else:
                    idx = dp.index(finish)
                    dp[idx] = i[1]
            res = max(res, len(dp))
        return res

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0 or len(intervals[0]) == 0:
            return 0
        
        res = 0
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        point_s = 0
        point_e = 0
        while point_s < len(start):
            if start[point_s] >= end[point_e]:
                res -= 1
                point_e += 1
            res += 1
            point_s += 1
        return res

# 1089. Duplicate Zeros
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        point = 0
        while point < len(arr):
            if arr[point] != 0:
                point += 1
            else:
                if point == len(arr)-1:
                    break
                elif point == len(arr)-2:
                    arr[point+1] = 0
                    break
                else:
                    for i in range(len(arr)-2, point, -1):
                        arr[i+1] = arr[i]
                    arr[point+1] = 0
                    point += 2

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        valid_zero = 0
        idx = len(arr)-1
        for i in range(idx+1):
            if i > idx - valid_zero:
                break
            if arr[i] == 0:
                if i == idx-valid_zero:
                    arr[idx] = 0
                    idx = idx - 1
                    break
                valid_zero += 1
        
        last = idx - valid_zero
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+valid_zero] = 0
                valid_zero -= 1
                arr[i+valid_zero] = 0
            else:
                arr[i+valid_zero] = arr[i]

# 1099. Two Sum Less Than K
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if len(A) <= 1:
            return -1
        A.sort()
        if A[0]+A[1] >= K:
            return -1
        l = 0
        r= len(A)-1
        res = -1
        while l < r:
            if A[l]+A[r] >= K:
                r -= 1
            else:
                res = max(res, A[l]+A[r])
                l += 1
        return res

# 1103. Distribute Candies to People
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        if num_people == 1:
            return [candies]
        if candies == 0:
            return [0]*num_people
        base = ((num_people+1)*num_people)//2
        increase = num_people**2
        res = [0]*num_people
        remain = candies
        for k in range(1,candies+1):
            new = base + increase*(k-1)
            if new <= remain:
                remain = remain-new
                continue
            else:
                break
        full_round = k-1
        res = [i*full_round+num_people*(((full_round-1+1)*(full_round-1))//2) for i in range(1,num_people+1)]
        remain = candies - sum(res)
        for i in range(1,num_people+1):
            if remain >= i+num_people*full_round:
                res[i-1] = res[i-1]+i+num_people*full_round
                remain -= i+num_people*full_round
            else:
                res[i-1] = res[i-1]+remain
                break
        return res
