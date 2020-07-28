# 1323. Maximum 69 Number
class Solution:
    def maximum69Number (self, num: int) -> int:
        res = list(str(num))
        for i in range(len(res)):
            if res[i] == '6':
                res[i] = '9'
                return int(''.join(res))
        return num

# 1331. Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []

        arr_sort = sorted(arr)
        store = {}
        curr = 1
        store[arr_sort[0]] = curr
        for i in range(1, len(arr_sort)):
            if arr_sort[i] == arr_sort[i-1]:
                continue
            else:
                curr += 1
                store[arr_sort[i]] = curr
        
        return [store[val] for val in arr]

# 1337. The K Weakest Rows in a Matrix
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            res.append(((sum(mat[i])), i))
        
        res.sort(key=lambda x: (x[0], [1]))
        return [res[i][1] for i in range(k)]

class Solution: # vertical search
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        
        res = []
        for j in range(col):
            for i in range(row):
                if mat[i][j] == 0 and i not in res:
                    res.append(i)
                if len(res) == k:
                    return res
        
        l = 0
        while len(res) < k:
            if mat[l][-1] == 1:
                res.append(l)
            l += 1
        return res

# 1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num >> 1
            else:
                num -= 1
            count += 1
        return count

class Solution:
    def numberOfSteps (self, num: int) -> int:
        bitnum = bin(num)[2:]
        return bitnum.count('1')*2+bitnum.count('0')-1

# 1346. Check If N and Its Double Exist
class Solution: #caution: 0
    def checkIfExist(self, arr: List[int]) -> bool:
        store = {}
        for i in range(len(arr)):
            if arr[i] not in store:
                store[arr[i]] = [i]
            else:
                store[arr[i]].append(i)
        for i in range(len(arr)):
            val = arr[i] * 2
            if val in store:
                for idx in store[val]:
                    if i != idx:
                        return True
        return False
