# 1408. String Matching in an Array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res = []
        for i in range(len(words)-1):
            sub = words[i]
            remain = '_'.join(words[i+1:])
            if sub in remain:
                res.append(sub)
        return res

# 1413. Minimum Value to Get Positive Step by Step Sum
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 1 - nums[-1]
        for i in range(len(nums)-2, -1, -1):
            val = nums[i]
            res = max(res-val, 1-val)
        return res if res>0 else 1

# 1417. Reformat The String
class Solution:
    def reformat(self, s: str) -> str:
        a = ''
        d = ''
        for l in s:
            if l.isdigit():
                d += l
            else:
                a += l
        if abs(len(a)-len(d)) > 1:
            return ''
        elif len(a) == len(d):
            res = ''
            for m, n in zip(a,d):
                res += m+n
            return res
        elif len(a) > len(d):
            res = a[0]
            for m, n in zip(d, a[1:]):
                res += m+n
            return res
        else:
            res = d[0]
            for m, n in zip(a, d[1:]):
                res += m+n
            return res

# 1422. Maximum Score After Splitting a String
class Solution:
    def maxScore(self, s: str) -> int:
        start = s[0]
        if start == '0':
            score = 1 + s[1:].count('1')
        else:
            score = s[1:].count('1')
        res = score
        for i in range(1,len(s)-1):
            if s[i] == '0':
                score = score+1
                res = max(res, score)
            else:
                score = score-1
                res = max(res, score)
        return res

# 1426. Counting Elements
class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        arr.sort()
        res = 0
        curr = 1
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == prev+1:
                res += curr
                curr = 1
                prev = arr[i]
            elif arr[i] == prev:
                curr += 1
                prev = arr[i]
            else:
                curr = 1
                prev = arr[i]
        return res
