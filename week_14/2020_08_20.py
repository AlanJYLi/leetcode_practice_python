# 396. Rotate Function
class Solution: # exceed time limit
    def maxRotateFunction(self, A: List[int]) -> int:
        if A == []:
            return 0
        
        n = len(A)
        store = {}
        for v in A:
            if v not in store:
                store[v] = []
                for i in range(n):
                    store[v].append(v*i)
        
        res = float('-inf')
        for i in range(n):
            temp = 0
            for j in range(n):
                temp += store[A[(n-i+j)%n]][j]
            res = max(res,temp)
        return res

class Solution: # based on mathematic property
    def maxRotateFunction(self, A: List[int]) -> int:
        total_A = sum(A)
        res = sum([i*v for i,v in enumerate(A)])
        curr = res
        for i in range(len(A)-1, 0, -1):
            curr += total_A - len(A)*A[i]
            res = max(res, curr)
        return res

# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for v in num:
            while k > 0 and len(stack) > 0 and v < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(v)
        stack = stack[:-k] if k > 0 else stack
        return ''.join(stack).lstrip('0') or '0'

# 406. Queue Reconstruction by Height
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        h_sort = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        res = []
        for p in h_sort:
            res.insert(p[1], p)
        return res
