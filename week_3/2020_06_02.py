# 346. Moving Average from Data Stream
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.windowsize = size
        self.nums = []

    def next(self, val: int) -> float:
        if len(self.nums) < self.windowsize:
            self.nums.append(val)
            return sum(self.nums) / len(self.nums)
        else:
            self.nums = self.nums[1:] + [val]
            return sum(self.nums) / len(self.nums)

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.windowsize = size
        self.nums = []
        self.count = 0
        self.movingsum = 0

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.count += 1
        start = self.nums.pop(0) if self.count>self.windowsize else 0
        self.movingsum = self.movingsum + val - start
        return self.movingsum / len(self.nums)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]

# 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store1 = {}
        store2 = {}
        for x in nums1:
            if x not in store1:
                store1[x] = 1
            else:
                store1[x] += 1
        for x in nums2:
            if x not in store2:
                store2[x] = 1
            else:
                store2[x] += 1
        
        res = []
        if len(store1) < len(store2):
            for x in store1:
                if x in store2:
                    res = res + [x] * min(store1[x], store2[x])
        else:
            for x in store2:
                if x in store1:
                    res = res + [x] * min(store1[x], store2[x])
        
        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        
        res = []
        i = 0
        j = 0
        while i<len(sorted1) and j<len(sorted2):
            if sorted1[i] < sorted2[j]:
                i += 1
            elif sorted1[i] == sorted2[j]:
                res.append(sorted1[i])
                i += 1
                j += 1
            else:
                j += 1
        return res

# 359. Logger Rate Limiter
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.record:
            self.record[message] = timestamp
            return True
        else:
            if timestamp < self.record[message] + 10:
                return False
            else:
                self.record[message] = timestamp
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l <= r:
            mid = (l+r) // 2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

# 374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        
        if guess(l) == 0:
            return l
        if guess(r) == 0:
            return r
        
        while l<=r:
            mid = (l+r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                l = mid + 1
            else:
                r = mid - 1

# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        for l in magazine:
            if l not in store:
                store[l] = 1
            else:
                store[l] += 1
        for l in ransomNote:
            if l not in store:
                return False
            else:
                store[l] -= 1
                if store[l] < 0:
                    return False
        return True

# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        for l in s:
            if l not in store:
                store[l] = 1
            else:
                store[l] += 1
        for i in range(len(s)):
            if store[s[i]] == 1:
                return i
        return -1

# 389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        s_sort = sorted(s)
        t_sort = sorted(t)
        
        for i in range(len(s_sort)):
            if s_sort[i] != t_sort[i]:
                return t_sort[i]
        return t_sort[i+1]

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        store = {}
        for l in s:
            if l not in store:
                store[l] = 1
            else:
                store[l] += 1
        
        for l in t:
            if l not in store or store[l] == 0:
                return l
            else:
                store[l] -= 1

# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True
        
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                j += 1
                i += 1
            else:
                j += 1
        
        return i == len(s)

# 401. Binary Watch
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        minute = {}
        hour = {}
        for i in range(60):
            b_num = bin(i).split('b')[-1]
            count = b_num.count('1')
            if count not in minute:
                minute[count] = [i]
            else:
                minute[count].append(i)
            
            if i < 12:
                if count not in hour:
                    hour[count] = [i]
                else:
                    hour[count].append(i)
        
        def gettime(h_num, m_num):
            hour_option = hour[h_num]
            minute_option = minute[m_num]
            res = []
            for h in hour_option:
                for m in minute_option:
                    time = str(h)+':'+str(m) if m>=10 else str(h)+':'+str(0)+str(m)
                    res.append(time)
            return res
        
        res = []
        for i in range(4):
            j = num-i
            if j >=0 and j<=5:
                res = res + gettime(i, j)
        return res

# 404. Sum of Left Leaves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # iteration
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        if root is None:
            return total
        
        stack = [root]    
        while len(stack) > 0:
            curr = stack.pop(-1)
            if curr.left is not None:
                if curr.left.left is None and curr.left.right is None:
                    total += curr.left.val
                else:
                    stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return total

class Solution: # recursion
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def process(root, is_left):
            if root.left is None and root.right is None:
                return root.val if is_left == True else 0
            
            total = 0
            if root.left is not None:
                total += process(root.left, True)
            if root.right is not None:
                total += process(root.right, False)
            return total
        
        return process(root, False)    

# 405. Convert a Number to Hexadecimal
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        if num < 0:
            num = 2**32+num
        
        base = ord('a')
        new = ''
        while num > 0:
            remain = num % 16
            num = num // 16
            if remain < 10:
                new = str(remain) + new
            else:
                new = chr(base-10+remain) + new
        return new







