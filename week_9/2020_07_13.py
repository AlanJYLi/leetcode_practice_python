# 1119. Remove Vowels from a String
class Solution:
    def removeVowels(self, S: str) -> str:
        a = {'a','e','i','o','u'}
        res = ''
        for s in S:
            if s not in a:
                res += s
        return res

# 1122. Relative Sort Array
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr2) == 0:
            return sorted(arr1)
        
        seen = {}
        notseen = []
        for num in arr2:
            seen[num] = []
        
        for num in arr1:
            if num in seen:
                seen[num].append(num)
            else:
                notseen.append(num)
        
        res = []
        for num in arr2:
            res = res + seen[num]
        
        return res+sorted(notseen)

# 1128. Number of Equivalent Domino Pairs
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        store = {}
        for a,b in dominoes:
            p =(a,b) if a<=b else (b,a)
            if p in store:
                store[p] += 1
            else:
                store[p] = 1
        
        res = 0
        if len(store) == 0:
            return res
        else:
            for p in store:
                if store[p] > 1:
                    res += (store[p]-1)*store[p]/2
            return int(res)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        store = {}
        res = 0
        for a,b in dominoes:
            p =(a,b) if a<=b else (b,a)
            if p in store:
                res += store[p]
                store[p] += 1
            else:
                store[p] = 1
        return res

# 1133. Largest Unique Number
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        seen = set()
        notseen = set()
        for num in A:
            if num not in seen and num not in notseen:
                notseen.add(num)
            elif num in notseen and num not in seen:
                notseen.remove(num)
                seen.add(num)
        return max(notseen) if len(notseen)>0 else -1

# 1134. Armstrong Number
class Solution:
    def isArmstrong(self, N: int) -> bool:
        res = 0
        target = N
        p = len(str(N))
        while N > 0:
            res += (N%10)**p
            N = N // 10
        return res == target

# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        store = {0:0,1:1,2:1}
        if n in store:
            return store[n]
        else:
            for i in range(3,n+1):
                store[i] = store[i-1]+store[i-2]+store[i-3]
            return store[n]