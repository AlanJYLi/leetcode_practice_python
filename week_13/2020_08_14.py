# 343. Integer Break
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+3)
        dp[2] = 1
        dp[3] = 2
        
        if n <= 3:
            return dp[n]
        
        for i in range(4, n+1):
            for j in range(1, i//2 + 1):
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        return dp[n]

# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        store = {}
        for n in nums:
            store[n] = store[n]+1 if n in store else 1
        temp = sorted(store.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][0])
        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        res = [set() for _ in range(len(nums))]
        for n in nums:
            if n not in store:
                store[n] = 1
                res[0].add(n)
            else:
                res[store[n]-1].remove(n)
                store[n] += 1
                res[store[n]-1].add(n)
        ans = []
        for i in range(len(res)-1, -1, -1):
            vals = res[i]
            if len(vals) == 0:
                continue
            else:
                k = k-len(vals)
                ans = ans + list(vals)
            if k == 0:
                return ans

# 356. Line Reflection
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        store = {}
        for x, y in points:
            if y not in store:
                store[y] = set()
                store[y].add(x)
            else:
                store[y].add(x)
        
        p = list(store.values())
        temp = sorted(p[0])
        if len(temp) == 1:
            x = temp[0]
        else:
            x = (temp[0] + temp[-1]) / 2
        
        for i in range(len(p)):
            temp = sorted(p[i])
            l = 0
            r = len(temp)-1
            while l <= r:
                if x != (temp[l] + temp[r]) / 2:
                    return False
                else:
                    l += 1
                    r -= 1
        return True

# 357. Count Numbers with Unique Digits
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        store = {1: 10}
        for i in range(2, n+1):
            fact = 1
            start = 9
            j = 1
            while j < i:
                fact *= start
                start -= 1
                j += 1
            store[i] = 9 * fact
        return sum(store.values())

# 360. Sort Transformed Array
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            if b >= 0:
                return [b*x+c for x in nums]
            else:
                return [b*x+c for x in reversed(nums)]
        
        mid = -b/2/a
        if mid <= nums[0]:
            res = [a*x**2+b*x+c for x in nums]
            if a > 0:
                return res
            else:
                return reversed(res)
        elif mid >= nums[-1]:
            res = [a*x**2+b*x+c for x in nums]
            if a > 0:
                return reversed(res)
            else:
                return res
        else:
            for i in range(1,len(nums)):
                if nums[i] < mid:
                    continue
                else:
                    l = i-1
                    r = i
                    break
            res = []
            while l >= 0 and r < len(nums):
                if abs(nums[l]-mid) >= abs(nums[r]-mid):
                    res.append(a*nums[r]**2+b*nums[r]+c)
                    r += 1
                else:
                    res.append(a*nums[l]**2+b*nums[l]+c)
                    l -= 1
            if l >= 0:
                while l >= 0:
                    res.append(a*nums[l]**2+b*nums[l]+c)
                    l -= 1
            if r < len(nums):
                while r < len(nums):
                    res.append(a*nums[r]**2+b*nums[r]+c)
                    r += 1
            if a > 0:
                return res
            else:
                return reversed(res)

