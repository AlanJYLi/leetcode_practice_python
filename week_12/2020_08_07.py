# 254. Factor Combinations
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        def process(n, subset, start, res):
            while start*start <= n:
                if n % start == 0:
                    res.append(subset+[start, n//start])
                    process(n//start, subset+[start], start, res)
                start += 1
            return
        
        res = []
        process(n, [], 2, res)
        return res

# 255. Verify Preorder Sequence in Binary Search Tree
class Solution: # exceed time limit
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        def process(preorder):
            if len(preorder) <= 2:
                return True
            else:
                root = preorder[0]
                i = 1
                while i < len(preorder):
                    if preorder[i] < root:
                        i += 1
                    else:
                        break
                idx = i-1
                if idx+1 <= len(preorder)-1 and min(preorder[idx+1:]) < root:
                    return False
                return process(preorder[1:idx+1]) and process(preorder[idx+1:])
        
        return process(preorder)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = float(-inf)
        for num in preorder:
            if num < lower:
                return False
            while len(stack)>0 and num > stack[-1]:
                lower = stack.pop()
            stack.append(num)
        return True

# 259. 3Sum Smaller
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        twosumtarget = [target-n for n in nums]
        
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                twosum = nums[i] + nums[j]
                for k in range(j+1, len(nums)):
                    if twosum < twosumtarget[k]:
                        count += 1
        return count

# 260. Single Number III
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return list(seen)

# 264. Ugly Number II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(1, n):
            nextugly = min(nums[p2]*2, nums[p3]*3, nums[p5]*5)
            nums.append(nextugly)
            
            if nextugly == nums[p2]*2:
                p2 += 1
            if nextugly == nums[p3]*3:
                p3 += 1
            if nextugly == nums[p5]*5:
                p5 += 1
        
        return nums[-1]

# 267. Palindrome Permutation II
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        def backtrack(first=0):
            if first == len(arr):
                p.append(''.join(arr[:]))
            else:
                used = set()
                for i in range(first, len(arr)):
                    if arr[i] in used:
                        continue
                    else:
                        used.add(arr[i])
                        arr[first], arr[i] = arr[i], arr[first]
                        backtrack(first+1)
                        arr[first], arr[i] = arr[i], arr[first]
                
        seen = set()
        arr = []
        for l in s:
            if l in seen:
                seen.remove(l)
                arr.append(l)
            else:
                seen.add(l)
        
        if len(seen) > 1:
            return []
        
        single = '' if len(seen) == 0 else list(seen)[0]
        
        p = []
        backtrack(0)
        
        res= []
        for sub in p:
            res.append(sub+single+sub[::-1])
        return res

# 277. Find the Celebrity
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        def check(i, n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True
        
        possible = 0
        for i in range(1, n):
            if knows(possible, i):
                possible = i
        
        if check(possible, n):
            return possible
        return -1
