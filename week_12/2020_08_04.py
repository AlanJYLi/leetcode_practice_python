# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = res[i-1] + nums[i]
        return res

# 1481. Least Number of Unique Integers after K Removals
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        store = {}
        for n in arr:
            store[n] = 1 if n not in store else store[n]+1
        count = list(store.values())
        count.sort(reverse=True)
        while k > 0:
            remove = count.pop()
            k -= remove
        if k == 0:
            return len(count)
        else:
            return len(count)+1

# 1482. Minimum Number of Days to Make m Bouquets
class Solution: # exceed time limit
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        state = ['o' for _ in range(len(bloomDay))]
        days = sorted(set(bloomDay))
        
        target = 'x'*k
        bloomed = set()
        for d in days:
            i = 0
            while i < len(bloomDay):
                if i not in bloomed and bloomDay[i] == d:
                    state[i] = 'x'
                    bloomed.add(i)
                i += 1
            if ''.join(state).count(target) >= m:
                return d

class Solution: # binary search. exceed time limit
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def num_day_t(t):
            adjacent = 0
            count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= t:
                    adjacent += 1
                    if adjacent == k:
                        count += 1
                        adjacent = 0
                else:
                    adjacent = 0
            return count
        
        if m*k > len(bloomDay):
            return -1
        
        days = sorted(set(bloomDay))
        l = 0
        r = len(days)
        while l <= r:
            mid = (l+r)//2
            if num_day_t(days[mid]) >= m:
                r -= 1
            else:
                l += 1
        return days[l]

# 1485. Clone Binary Tree With Random Pointer
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if root is None:
            return None
        
        queue = [root]
        store = {}
        while len(queue) > 0:
            node = queue.pop(0)
            newnode = NodeCopy(node.val)
            store[node] = newnode
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        for node, newnode in store.items():
            if node.random is not None:
                newnode.random = store[node.random]
            if node.left is not None:
                newnode.left = store[node.left]
            if node.right is not None:
                newnode.right = store[node.right]
        return store[root]

# 1488. Avoid Flood in The City
class Solution: # exceed time limit
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1 for _ in range(len(rains))]
        
        stack = []  #store (idx, lakenum/drynum)
        full = set()
        for i, val in enumerate(rains):
            if val > 0:
                if val not in full:
                    full.add(val)
                    stack.append((i, val))
                else:
                    back = []
                    temp = stack.pop()
                    while temp[1] != val and len(stack) > 0:
                        back.append(temp)
                        temp = stack.pop()
                    dry = False
                    while len(back) > 0:
                        temp = back.pop()
                        if temp[1] > 0:
                            stack.append(temp)
                        elif temp[1] == -1 and dry == False:
                            dry = True
                            res[temp[0]] = val
                        elif temp[1] == -1 and dry == True:
                            stack.append(temp)
                    if dry == False:
                        return []
                    else:
                        stack.append((i, val))
            else:
                stack.append((i, -1))
        while len(stack) > 0:
            temp = stack.pop()
            if temp[1] == -1:
                res[temp[0]] = 1
        return res

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry = []
        flood = {}
        res = []
        for idx, val in enumerate(rains):
            if val == 0:
                dry.append(idx)
                res.append(1)
            else:
                if val in flood:
                    dried = False
                    for j, pos in enumerate(dry):
                        if pos > flood[val]:
                            res[pos] = val
                            flood[val] = idx
                            dry.pop(j)
                            dried = True
                            break
                    if dried == False:
                        return []
                else:
                    flood[val] = idx
                res.append(-1)
        return res
