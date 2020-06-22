# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(s, t):
            l = 0
            r = len(s)-1
            if t < s[0]:
                return 'out left'
            elif t > s[r]:
                return 'out right'
            else:
                while l<=r:
                    mid = (l+r)//2
                    if s[mid] == t:
                        return True
                    elif s[mid] > t:
                        r = mid-1
                    else:
                        l = mid+1
                return False
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        elif target < matrix[0][0]:
            return False
        else:
            j = 0
            while j < len(matrix):
                s = matrix[j]
                res = searchRow(s, target)
                if res == 'out right':
                    j += 1
                elif res == 'out left':
                    return False
                else:
                    return res
            return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m*n-1
        while l<=r:
            mid = (l+r)//2
            num = matrix[mid//n][mid%n]
            if num == target:
                return True
            elif num > target:
                r = mid-1
            else:
                l = mid+1
        return False

# 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for num in nums:
            count[num] += 1
        start = 0
        for j in range(len(count)):
            c = count[j]
            for i in range(start, start+c):
                nums[i] = j
            start = start+c
        return nums

class Solution: # one-pass algorithm
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b0 = 0 # rightmost boundary of zero
        b2 = len(nums)-1 # leftmost boundary of two
        i = 0
        while i <= b2:
            num = nums[i]
            if num == 0:
                nums[b0], nums[i] = nums[i], nums[b0]
                i += 1
                b0 += 1
            elif num == 1:
                i += 1
            else:
                nums[b2], nums[i] = nums[i], nums[b2]
                b2 -= 1

# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) == 0:
            return ''
        
        store = {}
        for c in t:
            store[c] = 1 if c not in store else store[c]+1
        
        l = 0
        r = 0
        
        complete = 0
        window_count = {}
        res = float(inf), None, None
        
        while r < len(s):
            c = s[r]
            window_count[c] = 1 if c not in window_count else window_count[c]+1
            if c in store and store[c] == window_count[c]:
                complete += 1
            
            while l <= r and complete == len(store):
                if r-l+1 < res[0]:
                    res = (r-l+1, l, r)
                
                c = s[l]
                window_count[c] -= 1
                if c in store and store[c] > window_count[c]:
                    complete -= 1
                
                l += 1
            
            r += 1
        
        return '' if res[1] is None else s[res[1]:res[2]+1]

# 77. Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        
        res = []
        backtrack()
        return res

# 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=0, curr=[]):
            if tuple(curr[:]) not in seen:
                res.append(curr[:])
                seen.add(tuple(curr[:]))
            for i in range(first, len(nums)):
                num = nums[i]
                curr.append(num)
                backtrack(i+1, curr)
                curr.pop()
        
        res = []
        seen = set()
        backtrack()
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                temp = res[i][:] + [num]
                res.append(temp)
        return res

# 79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(r, c, s):
            if s == '':
                return True
            if r < 0 or r == self.R or c < 0 or c == self.C or board[r][c] != s[0]:
                return False
            
            state = False
            board[r][c] = '#'
            for move_r, move_c in [(0,1),(1,0),(0,-1),(-1,0)]:
                state = backtrack(r+move_r, c+move_c, s[1:])
                if state == True:
                    break
            
            board[r][c] = s[0]
            return state
        
        self.R = len(board)
        self.C = len(board[0])
        for i in range(self.R):
            for j in range(self.C):
                if backtrack(i, j, word) == True:
                    return True
        return False

# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return len(nums)
        else:
            read = 1
            write = 1
            count = 1
            while read < len(nums):
                if nums[read] == nums[read-1] and count == 1:
                    nums[write] = nums[read]
                    read += 1
                    write += 1
                    count += 1
                elif nums[read] == nums[read-1] and count == 2:
                    read += 1
                elif nums[read] != nums[read-1]:
                    nums[write] = nums[read]
                    read += 1
                    write += 1
                    count = 1
            if count == 2:
                nums[write-1] = nums[read-1]
            return write

# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            else:
                i = mid-1
                while i >= l and nums[i] == nums[mid]:
                    i -= 1
                midleft = i
                j = mid+1
                while j <= r and nums[j] == nums[mid]:
                    j += 1
                midright = j
                
                if nums[mid] > nums[l]:
                    if nums[l] <= target <= nums[mid]:
                        r = midleft
                    else:
                        l = midright
                elif nums[mid] < nums[l]:
                    if nums[mid] <= target <= nums[r]:
                        l =midright
                    else:
                        r = midleft
                else:
                    if midleft < l:
                        l = midright
                    if midright > r:
                        r = midleft
        return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def process(l, r):
            if r < l:
                return False
            if r == l:
                return nums[l] == target
            
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l]<=target<nums[mid]:
                    return process(l,mid-1)
                else:
                    return process(mid+1,r)
            elif nums[mid] < nums[r]:
                if nums[mid]<target<=nums[r]:
                    return process(mid+1,r)
                else:
                    return process(l,mid-1)
            else:
                return process(l,mid-1) or process(mid+1,r)
        
        return process(0,len(nums)-1)

# 82. Remove Duplicates from Sorted List II
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        new = dummy
        curr = head
        temp = head.next
        duplicate = False
        while temp is not None:
            if temp.val != curr.val:
                if duplicate == True:
                    curr = temp
                    temp = temp.next
                    duplicate = False
                else:
                    new.next = curr
                    new = new.next
                    curr = temp
                    temp = temp.next
            else:
                temp = temp.next
                duplicate = True
        if duplicate == False:
            new.next = curr
        else:
            new.next = temp
        return dummy.next

# 84. Largest Rectangle in Histogram
class Solution: # brute force: exceed time limit
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            lowest = float(inf)
            for j in range(i, len(heights)):
                lowest = min(lowest, heights[j])
                res = max(res, lowest*(j-i+1))
        return res

class Solution: # divide and conqure: exceed time limit
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def process(l, r):
            if l > r:
                return 0
            
            minindex = l
            for i in range(l, r+1):
                if heights[i] < heights[minindex]:
                    minindex = i
            
            curr = (r-l+1) * heights[minindex]
            return max(curr, max(process(l, minindex-1), process(minindex+1, r)))
        
        return process(0,len(heights)-1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1,-1)]
        res = 0
        for i in range(len(heights)):
            while stack[-1][0] != -1 and stack[-1][1] >= heights[i]:
                index, h = stack.pop()
                res = max(res, h*(i-stack[-1][0]-1))
            stack.append((i, heights[i]))
        while stack[-1][0] != -1:
            index, h = stack.pop()
            res = max(res, h*(len(heights)-stack[-1][0]-1))
        return res