# 1490. Clone N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        queue = [root]
        store = {}
        while len(queue) > 0:
            curr = queue.pop(0)
            newnode = Node(curr.val)
            store[curr] = newnode
            
            if curr.children != []:
                for c in curr.children:
                    queue.append(c)
        
        for old, new in store.items():
            if old.children != []:
                for c in old.children:
                    new.children.append(store[c])
        
        return store[root]

# 1491. Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        if salary[0] < salary[1]:
            low, high = salary[0], salary[1]
        else:
            low, high = salary[1], salary[0]
        
        total = 0
        for num in salary[2:]:
            if num < low:
                total += low
                low = num
            elif num > high:
                total += high
                high = num
            else:
                total += num
        return total/(len(salary)-2)

# 1492. The kth Factor of n
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        root = sqrt(n)
        root_int = floor(root)
        for i in range(1, root_int+1):
            if n % i == 0:
                if i**2 != n:
                    small.append(i)
                    large.append(n//i)
                else:
                    small.append(i)
        if k <= len(small):
            return small[k-1]
        elif k > len(small)+len(large):
            return -1
        else:
            return large[-(k-len(small))]

# 1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        res = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                res.append(0)
                i += 1
            else:
                j = i+1
                while j < len(nums) and nums[j] != 0:
                    j += 1
                res.append(j-i)
                i = j
        if len(res) == 1:
            return res[0]-1
        elif len(res) == 2:
            return sum(res)
        else:
            l = 0
            for i in range(len(res)-2):
                l = max(l, res[i]+res[i+2])
            return l

# 1496. Path Crossing
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        h,v = 0,0
        visited = set()
        visited.add((0,0))
        for d in path:
            if d == 'N':
                v += 1 
            elif d == 'S':
                v -= 1
            elif d == 'E':
                h += 1
            else:
                h -= 1
            
            if (h,v) in visited:
                return True
            else:
                visited.add((h,v))
        return False
