# 1002. Find Common Characters
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if A == []:
            return []
        n = len(A)
        mark = [[0]*n for i in range(26)]
        
        for i in range(n):
            w = A[i]
            for s in w:
                mark[ord(s)-ord('a')][i] += 1
        
        res = []
        for i in range(26):
            temp = min(mark[i])
            if temp > 0:
                res = res + [chr(ord('a')+i)]*temp
        return res

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if A == []:
            return []
        store = {}
        for i in range(26):
            store[chr(ord('a')+i)] = 0
        
        for s in store:
            count = min([w.count(s) for w in A])
            store[s] = count
        
        res = []
        for s in store:
            if store[s] > 0:
                res += [s]*store[s]
        return res

# 1005. Maximize Sum Of Array After K Negations
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        def getmin(A):
            temp = A[0]
            i = 0
            for j in range(1,len(A)):
                if A[j] < temp:
                    temp = A[j]
                    i = j
            return temp, i
        
        while K > 0:
            temp, i = getmin(A)
            A[i] = -A[i]
            K -= 1
        
        return sum(A)

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while K > 0 and A[i] < 0:
            A[i] = -A[i]
            K -= 1
            i += 1
        
        if K % 2 == 0:
            return sum(A)
        else:
            return sum(A) - 2*min(A[i-1],A[i])

# 1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        l = len(bin(N).split('b')[-1])
        mask = (1 << l)-1
        return mask^N

# 1010. Pairs of Songs With Total Durations Divisible by 60
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        store = {}
        for t in time:
            r = t % 60
            if r not in store:
                store[r] = 1
            else:
                store[r] += 1
        res = 0
        for r in store:
            if 0 < r < 30:
                if 60-r in store:
                    res += store[r]*store[60-r]
            elif r == 30 or r == 0:
                res += store[r]*(store[r]-1)//2
        return res

# 1013. Partition Array Into Three Parts With Equal Sum
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        total = sum(A)
        if total % 3 != 0:
            return False
        target = total // 3
        i = 0
        sum1 = 0
        while i < len(A):
            sum1 += A[i]
            if sum1 != target:
                i += 1
            else:
                break
        if i == len(A) or i == len(A)-1 or i == len(A)-2:
            return False
        j = len(A)-1
        sum2 = 0
        while j > i:
            sum2 += A[j]
            if sum2 != target:
                j -= 1
            else:
                break
        if j == i or j == i+1:
            return False
        return sum(A[i+1:j]) == target

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        total = sum(A)
        if total % 3 != 0:
            return False
        target = total // 3
        part = 0
        temp = 0
        for a in A[:-1]:
            temp += a
            if temp == target:
                if part == 1:
                    return True
                temp = 0
                part = 1
        return False
