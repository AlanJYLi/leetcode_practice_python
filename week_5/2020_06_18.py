# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findSorted(nums, target, start_index):
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return start_index+mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] >= nums[0] and nums[mid] <= nums[-1]:
                # nums is sorted
                return findSorted(nums, target, 0)
            elif nums[mid] >= nums[0] and nums[mid] > nums[-1]:
            	# left part is sorted
                res = findSorted(nums[start:mid+1], target, start)
                if res != -1:
                    return res
                else:
                    start = mid + 1
            elif nums[mid] < nums[0] and nums[mid] <= nums[-1]:
            	# right part is sorted
                res = findSorted(nums[mid:end+1], target, mid)
                if res != -1:
                    return res
                else:
                    end = mid-1
        return -1

class Solution: # one pass
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1

# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findleft(nums, target):
            res = -1
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    res = mid
                    r = mid-1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return res
        
        def findright(nums, target):
            res = -1
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    res = mid
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return res
        
        if len(nums) == 0:
            return [-1,-1]
        return [findleft(nums, target), findright(nums,target)]

# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        column = [set() for i in range(9)]
        cell = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in row[i]:
                        return False
                    else:
                        row[i].add(num)
                    if num in column[j]:
                        return False
                    else:
                        column[j].add(num)
                    
                    cellnum = (i//3)*3 + j//3
                    if num in cell[cellnum]:
                        return False
                    else:
                        cell[cellnum].add(num)
        return True

# 37. Sudoku Solver
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(9)]
        column = [set() for i in range(9)]
        cell = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row[i].add(num)
                    column[j].add(num)
                    cellnum = (i//3)*3 + j//3
                    cell[cellnum].add(num)
        
        def can_fill(d, r, c):
            cellnum = r//3*3+c//3
            return d not in row[r] and d not in column[c] and d not in cell[cellnum]
        
        def track(r, c):
            if r == 8 and c == 9:
                return True
            elif r < 8 and c == 9:
                c = 0
                r += 1
            
            if board[r][c] != '.':
                return track(r, c+1)
            
            cellnum = r//3*3+c//3
            for val in range(1, 10):
                v = str(val)
                if can_fill(v, r, c) == False:
                    continue
                
                board[r][c] = v
                row[r].add(v)
                column[c].add(v)
                cell[cellnum].add(v)
                
                if track(r, c+1) == True:
                    return True
                
                board[r][c] = '.'
                row[r].remove(v)
                column[c].remove(v)
                cell[cellnum].remove(v)
            return False
        
        track(0,0)

# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            l = 0
            r = len(nums)-1
            res = set()
            while l<r:
                if nums[l] + nums[r] == target:
                    res.add((nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return [x for x in map(list, res)]
        
        def oneSum(nums, target):
            if target in set(nums):
                return [target]
            else:
                return []
        
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0]*k>target or nums[-1]*k<target:
                return res
            if k == 1:
                return [oneSum(nums, target)]
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    s = kSum(nums[i+1:], target-nums[i], k-1)
                    for num_list in s:
                        res.append([nums[i]]+num_list)
            return res
        
        full_candidates = []
        for num in candidates:
            full_candidates += [num] * (target//num)
        full_candidates.sort()
        res = []
        for k in range(1,len(full_candidates)+1):
            solution = kSum(full_candidates, target, k)
            for l in solution:
                if l != []:
                    res.append(l)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        
        store = {}
        for c in candidates:
            for i in range(1, target+1):
                if c == i:
                    if i not in store:
                        store[i] = [[c]]
                    else:
                        store[i] += [[c]]
                elif i-c > 0 and i-c in store:
                    for num_list in store[i-c]:
                        x = num_list + [c]
                        if i not in store:
                            store[i] = [x]
                        else:
                            store[i].append(x)
        
        if target not in store:
            return []
        else:
            return store[target]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, nums):
            if sum(curr) > target:
                return
            elif sum(curr) == target:
                res.append(curr[:])
            
            for i in range(len(nums)):
                dfs(curr+[nums[i]], nums[i:])
        
        res = []
        dfs([], candidates)
        return res

# 40. Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, nums):
            if sum(curr) > target:
                return
            elif sum(curr) == target:
                res.append(curr)
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(curr+[nums[i]], nums[i+1:])
        
        res = []
        dfs([], sorted(candidates))
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        store = [set() for i in range(target+1)]
        store[0].add(())
        for c in sorted(candidates):
            for i in range(target, c-1, -1):
                if i >= c:
                    for seq in store[i-c]:
                        store[i].add(seq+(c,))
        return store[target]

# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        
        n = len(nums)
        if n == 1 and nums[0] == 1:
            return 2
        
        for i in range(n):
            if nums[i]<=0 or nums[i] > n:
                nums[i] = 1
        
        for i in range(n):
            temp = abs(nums[i])
            if temp == n:
                nums[0] = -abs(nums[0])
            else:
                nums[temp] = -abs(nums[temp])
        
        for i in range(1,n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
        
        return n+1

# 42. Trapping Rain Water
class Solution: # count layer by layer, but exceed the time limit
    def trap(self, height: List[int]) -> int:
        def getmin(height):
            res = float(inf)
            for n in height:
                if n > 0:
                    res = min(res, n)
            return res
        
        def getlayer(height, d):
            level = []
            for n in height:
                if n < d:
                    level.append(0)
                else:
                    level.append(1)
            return level
        
        def trap_in_layer(level, d):
            s = ''.join(map(str,level))
            s = s.split('1')
            if len(s) <= 2:
                return 0
            else:
                count = 0
                for i in range(1,len(s)-1):
                    count += len(s[i])
                return count*d
        
        def getremain(heigth, level, d):
            remain = []
            for i in range(len(height)):
                remain.append(height[i]-level[i]*d)
            return remain
        
        res = 0
        while sum(height) > 1:
            d = getmin(height)
            level = getlayer(height, d)
            height = getremain(height, level, d)
            res += trap_in_layer(level, d)
        return res

class Solution: # for each position, find the leftmat and rightmax, then water that can be trapped at this position is min(leftmax, rightmax) - height[i]
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        res = 0
        for i in range(len(height)):
            for j in range(i+1):
                leftmax = max(leftmax, height[j])
            for j in range(i,len(height)):
                rightmax = max(rightmax, height[j])
            res += min(leftmax, rightmax) - height[i]
            leftmax = 0
            rightmax = 0
        return res

class Solution: # dynamic programming: don't traverse again and again to find the leftmax and rightmax
    def trap(self, height: List[int]) -> int:
        leftmax = [-1]*len(height)
        rightmax = [-1]*len(height)
        for i in range(len(height)):
            if i == 0:
                leftmax[i] = height[i]
            else:
                leftmax[i] = max(leftmax[i-1], height[i])
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                rightmax[i] = height[i]
            else:
                rightmax[i] = max(rightmax[i+1], height[i])
        res = 0
        for i in range(len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res

class Solution: # two pointers; calculate on the run
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        leftmax = 0
        rightmax = 0
        res = 0
        while l<r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax < rightmax:
                res += leftmax-height[l]
                l += 1
            else:
                res += rightmax-height[r]
                r -= 1
        return res

# 43. Multiply Strings
# unclear requirement
# use dict to conver string to int or reverse

# 44. Wildcard Matching
class Solution: # similar as Q10, but exceed the time limit
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        elif s != '' and p == '':
            return False
        elif s == '' and p != '':
            return set(p) == {'*'}
        else:
            if p[0] != '*':
                match = bool(s) and p[0] in {s[0], '?'}
                return match and self.isMatch(s[1:], p[1:])
            else:
                return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)

class Solution:  # save the result of compare s[i:] and p[j:]
    def isMatch(self, s: str, p: str) -> bool:
        store = {}
        def process(i, j):
            if (i, j) not in store:
                if i == len(s) and j == len(p):
                    res = True
                elif i < len(s) and j == len(p):
                    res = False
                elif i == len(s) and j < len(p):
                    res = set(p[j:]) == {'*'}
                else:
                    if p[j] != '*':
                        match = i < len(s) and p[j] in {s[i], '?'}
                        res = match and process(i+1, j+1)
                    else:
                        res = process(i, j+1) or process(i+1, j)
                store[(i,j)] = res
            return store[(i,j)]
        
        return process(0,0)

class Solution: # more dynamic way: backtracking
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)
        si = 0
        pi = 0
        temp_star = -1
        temp_s = -1
        while si < sl:
            if pi < pl and p[pi] in {'?', s[si]}:
                si += 1
                pi += 1
            elif pi < pl and p[pi] == '*':
                temp_star = pi
                temp_s = si
                pi += 1
            elif temp_star == -1:
                return False
            else:
                pi = temp_star + 1
                si = temp_s + 1
                temp_s = si
        
        if pi == pl:
            return True
        else:
            return {'*'} == set(p[pi:])