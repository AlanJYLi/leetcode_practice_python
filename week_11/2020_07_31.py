# 1427. Perform String Shifts
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_shift = 0
        for d, step in shift:
            if d == 0:
                final_shift -= step
            else:
                final_shift += step
        
        final_shift = int(final_shift/abs(final_shift) * (abs(final_shift)%len(s)))
        if final_shift < 0:
            final_shift = len(s) + final_shift
        
        return s[-final_shift:] + s[:-final_shift]

# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxval = max(candies)
        res = []
        for num in candies:
            if num+extraCandies >= maxval:
                res.append(True)
            else:
                res.append(False)
        return res

# 1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        for i in range(len(paths)):
            start.add(paths[i][0])
        for i in range(len(paths)):
            if paths[i][1] not in start:
                return paths[i][1]

# 1441. Build an Array With Stack Operations
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        j = 1
        while i < len(target):
            val = target[i]
            while j < val:
                res.append('Push')
                res.append('Pop')
                j += 1
            res.append('Push')
            i += 1
            j += 1
        return res

# 1446. Consecutive Characters
class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        prev = s[0]
        count = 1
        for i in range(1,len(s)):
            if s[i] == prev:
                count += 1
            else:
                res = max(res, count)
                count = 1
                prev = s[i]
        return max(res,count)

