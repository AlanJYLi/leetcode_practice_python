# 687. Longest Univalue Path
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.path = 0
        
        def process(root):
            if root is None:
                return 0
            left = process(root.left)
            right = process(root.right)
            left_path = 0
            right_path = 0
            if root.left is not None and root.val == root.left.val:
                left_path = left + 1
            if root.right is not None and root.val == root.right.val:
                right_path = right + 1
            self.path = max(self.path, left_path+right_path)
            return max(left_path, right_path)
        
        process(root)
        return self.path

# 690. Employee Importance
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        store = {}
        for e in employees:
            store[e.id] = e
        
        def process(num):
            person = store[num]
            total = person.importance
            for eid in person.subordinates:
                total += process(eid)
            return total
        
        return process(id)

# 693. Binary Number with Alternating Bits
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        for i in range(1,len(b)):
            if b[i] == b[i-1]:
                return False
        return True

# 696. Count Binary Substrings
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        store = []
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                store.append(count)
                count = 1
        store.append(count)
        if len(store) <= 1:
            return 0
        else:
            res = 0
            for i in range(1,len(store)):
                res += min(store[i], store[i-1])
            return res

# 697. Degree of an Array
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        position = {}
        count = {}
        for i in range(len(nums)):
            if nums[i] not in position:
                position[nums[i]] = [i]
            else:
                position[nums[i]].append(i)
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        degree = max(count.values())
        res = float(inf)
        for n in count:
            if count[n] == degree:
                length = max(position[n])-min(position[n])+1
                res = min(res,length)
        return res

# 700. Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# 703. Kth Largest Element in a Stream
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if nums != []:
            self.array = sorted(nums, reverse=True)
            if len(self.array) >= self.k:
                self.kth = self.array[self.k-1]
            else:
                self.kth = self.array[-1]
        else:
            self.array = []
            self.kth = None

    def add(self, val: int) -> int:
        if self.kth is None:
            self.array.append(val)
            self.kth = val
            return val
        if val <= self.kth and len(self.array) < self.k:
            self.array.append(val)
            self.kth = val
            return val
        elif val <= self.kth and len(self.array) >= self.k:
            self.array.append(val)
            return self.kth
        else:
            l = 0
            r = self.k-1
            if self.array[0] <= val:
                self.array = [val] + self.array
            else:
                while r-l > 1:
                    mid = (l+r)//2
                    if self.array[mid] == val:
                        r = mid
                        break
                    elif self.array[mid] > val:
                        l = mid
                    else:
                        r = mid
                self.array = self.array[:r] + [val] + self.array[r:]
            self.kth = self.array[self.k-1]
            return self.kth

# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        else:
            if target <= nums[0]:
                return 0 if nums[0] == target else -1
            elif target >= nums[-1]:
                return len(nums)-1 if nums[-1] == target else -1
            else:
                l = 0
                r = len(nums)-1
                while r - l > 1:
                    mid = (r+l)//2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        r = mid
                    else:
                        l = mid
                return -1

# 709. To Lower Case
class Solution:
    def toLowerCase(self, str: str) -> str:
    	return str.lower()

class Solution:
    def toLowerCase(self, str: str) -> str:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        store = dict(zip(upper,lower))
        return ''.join([store[x] if x in store else x for x in str])

# 716. Max Stack
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # [(x, max_for_now)]

    def push(self, x: int) -> None:
        if self.stack == []:
            self.stack.append((x, x))
        else:
            max_num = max(self.stack[-1][1], x)
            self.stack.append((x, max_num))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]
        
    def peekMax(self) -> int:
        return self.stack[-1][1]
        
    def popMax(self) -> int:
        stack = []
        while self.stack[-1][0] != self.stack[-1][1]:
            stack.append(self.pop())
        
        max_num = self.stack[-1][1]
        self.pop()
        
        while len(stack) > 0:
            x = stack.pop()
            self.push(x)
        
        return max_num

# 717. 1-bit and 2-bit Characters
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        else:
            i = 0
            while i < len(bits)-1:
                if bits[i] == 0:
                    i += 1
                else:
                    i += 2
            return i == len(bits) - 1

# 720. Longest Word in Dictionary
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ''
        wordset = set(words)
        for w in words:
            if len(w) > len(res) or (len(w) == len(res) and w < res):
                if all([w[:k] in wordset for k in range(1,len(w))]):
                    res = w
        return res

# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        else:
            i = 0
            prev = nums[i]
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            while i < len(nums)-1:
                if left == right:
                    return i
                else:
                    i += 1
                    left = left + prev
                    prev = nums[i]
                    right = right - nums[i]
            return i if left == right else -1

class Solution: # cleaner code
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        else:
            total = sum(nums)
            left = 0
            for i, x in enumerate(nums):
                if left == total-left-x:
                    return i
                left = left + x
            return -1

# 728. Self Dividing Numbers
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if i < 10:
                res.append(i)
            else:
                if all([d != '0' and i % int(d) == 0 for d in str(i)]):
                    res.append(i)
        return res

# 733. Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        L = len(image)
        W = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        
        def process(l, w):
            if image[l][w] == color:
                image[l][w] = newColor
                if l >= 1:
                    process(l-1, w)
                if l+1 < L:
                    process(l+1, w)
                if w >= 1:
                    process(l, w-1)
                if w+1 < W:
                    process(l, w+1)
        
        process(sr,sc)
        return image

# 734. Sentence Similarity
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        else:
            store = set()
            for p in pairs:
                store.add(p[0]+'+'+p[1])
            for i in range(len(words1)):
                w1 = words1[i]
                w2 = words2[i]
                if w1 == w2:
                    continue
                elif w1+'+'+w2 in store or w2+'+'+w1 in store:
                    continue
                else:
                    return False
            return True

# 744. Find Smallest Letter Greater Than Target
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a = sorted(set(letters))
        if target < a[0] or target >= a[-1]:
            return a[0]
        elif target == a[0]:
            return a[1]
        else:
            l = 0
            r = len(a) - 1
            while r-l>1:
                mid = (l+r)//2
                if a[mid] == target:
                    return a[mid+1]
                elif a[mid] > target:
                    r = mid
                else:
                    l = mid
            return a[r]