# 209. Minimum Size Subarray Sum
class Solution: # exceed time limit
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        res = len(nums) + 1
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):
            dp[i] = dp[i-1]+nums[i]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                temp = dp[j] - dp[i] + nums[i]
                if temp >= s:
                    res = min(res, j-i+1)
                    if res == 1:
                        return res
        return res if res < len(nums)+1 else 0

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        res = len(nums)+1
        cusum = 0
        i = 0
        for j in range(len(nums)):
            cusum += nums[j]
            while cusum >=s:
                res = min(res, j-i+1)
                cusum -= nums[i]
                i += 1
        return res if res < len(nums)+1 else 0

# 210. Course Schedule II
class Solution: # use indegree
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        store = {}
        indegree = {}
        for curr, prev in prerequisites:
            if prev not in store:
                store[prev] = [curr]
            else:
                store[prev].append(curr)
            if curr not in indegree:
                indegree[curr] = 1
            else:
                indegree[curr] += 1
        
        path = []
        queue = []
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
            
        while len(queue) > 0:
            node = queue.pop(0)
            path.append(node)
            if node in store:
                for nextcourse in store[node]:
                    indegree[nextcourse] -= 1
                    
                    if indegree[nextcourse] == 0:
                        queue.append(nextcourse)
        return path if len(path) == numCourses else []

# 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        dp_withhead = [0] * len(nums)
        dp_nohead = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp_withhead[i] = nums[i]
            elif i == 1:
                dp_withhead[i] = dp_withhead[i-1]
                dp_nohead[i] = nums[i]
            elif i == 2:
                dp_withhead[i] = max(dp_withhead[i-2]+nums[i], dp_withhead[i-1])
                dp_nohead[i] = max(nums[i], dp_nohead[i-1])
            elif 2 < i < len(nums)-1:
                dp_withhead[i] = max(dp_withhead[i-2]+nums[i], dp_withhead[i-1])
                dp_nohead[i] = max(dp_nohead[i-2]+nums[i], dp_nohead[i-1])
            else:
                dp_withhead[i] = dp_withhead[i-1]
                dp_nohead[i] = max(dp_nohead[i-2]+nums[i], dp_nohead[i-1])
        return max(max(dp_withhead), max(dp_nohead))

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            prev, curr = curr, max(curr, prev+nums[i])
        max_head = curr
        
        prev = 0
        curr = nums[1]
        for i in range(2, len(nums)):
            prev, curr = curr, max(curr, prev+nums[i])
        max_nohead = curr
        
        return max(max_head, max_nohead)

# 214. Shortest Palindrome
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        
        rs = s[::-1]
        for i in range(len(s), 0, -1):
            if s[:i] == rs[len(s)-i:]:
                return rs[:len(s)-i] + s

# 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(k, n, t, cusum, first):
            if cusum > n:
                return 
            elif cusum == n and len(t) == k:
                res.append([]+t)
            else:
                for i in range(first,10):
                    t.append(i)
                    backtrack(k, n, t, cusum+i, i+1)
                    t.pop()
        
        res = []
        backtrack(k,n,[],0,1)
        return res