# 1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        store = {}
        arr.sort()
        minabs = float('inf')
        for i in range(len(arr)-1):
            temp = arr[i+1]-arr[i]
            if temp < minabs:
                store[temp] = [[arr[i],arr[i+1]]]
                minabs = temp
            elif temp == minabs:
                store[temp].append([arr[i],arr[i+1]])
            else:
                continue
        return store[minabs]

# 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        store = {}
        for n in arr:
            store[n] = store[n]+1 if n in store else 1
        v = list(store.values())
        return len(v) == len(set(v))

# 1213. Intersection of Three Sorted Arrays
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        i = 0
        j = 0
        k = 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                maxval = max([arr1[i], arr2[j], arr3[k]])
                if arr1[i] != maxval:
                    i += 1
                if arr2[j] != maxval:
                    j += 1
                if arr3[k] != maxval:
                    k += 1
        return res

# 1221. Split a String in Balanced Strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        count = 0
        for x in s:
            count = count+1 if x=='R' else count-1
            if count == 0:
                res += 1
        return res

# 1228. Missing Number In Arithmetic Progression
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return ((arr[0]+arr[-1])*(len(arr)+1))//2-sum(arr)

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if diff >= 0 and arr[i+1]-arr[i] > diff:
                return arr[i]+diff
            elif diff >=0 and arr[i+1]-arr[i] < diff:
                diff = arr[i+1]-arr[i]
                return arr[i]-diff
            elif diff < 0 and arr[i+1]-arr[i] > diff:
                diff = arr[i+1]-arr[i]
                return arr[i]-diff
            elif diff < 0 and arr[i+1]-arr[i] < diff:
                return arr[i]+diff
        return arr[0]

# 1232. Check If It Is a Straight Line
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        base = coordinates[0]
        vector = [coordinates[1][0]-base[0], coordinates[1][1]-base[1]]
        for i in range(2,len(coordinates)):
            p = coordinates[i]
            new_vector = [p[0]-base[0], p[1]-base[1]]
            if new_vector[0]*vector[1] != new_vector[1]*vector[0]:
                return False
        return True
