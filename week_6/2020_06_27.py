# 133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.seen = {}
        
        def process(node):
            if node is None:
                return node
            
            if node in self.seen:
                return self.seen[node]
            
            clone = Node(node.val,[])
            self.seen[node] = clone
            
            if node.neighbors is not None:
                clone.neighbors = [process(n) for n in node.neighbors]
            
            return clone
        
        return process(node)

# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [gas[i]-cost[i] for i in range(len(gas))]
        
        for i in range(len(remain)):
            if remain[i] < 0:
                continue
            else:
                j = 1
                cusum = remain[i]
                while j < len(remain):
                    nextone = remain[(i+j)%len(remain)]
                    cusum += nextone
                    if cusum >= 0:
                        j += 1
                    else:
                        break
                if j == len(remain):
                    return i
                else:
                    continue
        return -1

class Solution: # bidirection loop
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [gas[i]-cost[i] for i in range(len(gas))]
        
        back = len(remain)-1
        forward = 0
        cusum = remain[forward]
        while forward+1 <= back:
            if cusum >= 0:
                forward += 1
                cusum += remain[forward]
            else:
                cusum += remain[back]
                back -= 1
        if cusum >= 0:
            return (back+1)%len(remain)
        else:
            return -1

class Solution: # leetcode solution
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [gas[i]-cost[i] for i in range(len(gas))]
        
        total = 0
        curr = 0
        start = 0
        for i in range(len(remain)):
            total += remain[i]
            curr += remain[i]
            if curr < 0:
                start = i+1
                curr = 0
        return start if total >= 0 else -1

# 135. Candy # exceed time limit, if ratings is in decenting order
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)
        
        dp = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = 1+dp[i-1]
            if ratings[i] < ratings[i-1]:
                j = i
                while dp[j] == dp[j-1] and ratings[j] < ratings[j-1]:
                    dp[j-1] += 1
                    j -= 1
        return sum(dp)

class Solution: # two arrays
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)
        
        n = len(ratings)
        dp_left = [1]*n
        dp_right = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                dp_left[i] = dp_left[i-1]+1
            if ratings[n-1-i] > ratings[n-i]:
                dp_right[n-1-i] = dp_right[n-i]+1
        total = 0
        for i in range(n):
            total += max(dp_left[i],dp_right[i])
        return total

# 137. Single Number II
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = set()
        seen = set()
        for n in nums:
            if n not in seen and n not in store:
                store.add(n)
            elif n in seen:
                continue
            elif n in store and n not in seen:
                store.remove(n)
                seen.add(n)
        return list(store)[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = set(nums)
        return (3*sum(a)-sum(nums))//2

class Solution: # leetcode: to achieve constant space complexity
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        for n in nums:
            once = ~twice & (once^n)
            twice = ~once & (twice^n)
        return once

# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        store = {}
        old = head
        curr = Node(old.val, None, None)
        store[old] = curr
        
        while old is not None:
            if old.next is None:
                curr.next = None
            else:
                if old.next in store:
                    curr.next = store[old.next]
                else:
                    store[old.next] = Node(old.next.val, None, None)
                    curr.next = store[old.next]
    
            if old.random is None:
                curr.random = None
            else:
                if old.random in store:
                    curr.random = store[old.random]
                else:
                    store[old.random] = Node(old.random.val, None, None)
                    curr.random = store[old.random]
            
            old = old.next
            curr = curr.next
        
        return store[head]

# 139. Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        store = {}
        
        def process(start):
            if start == len(s):
                return True
            if start in store:
                return store[start]
            for i in range(start+1, len(s)+1):
                if s[start:i] in wd and process(i):
                    store[start] = True
                    return True
            store[start] = False
            return False
        return process(0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wd:
                    dp[i] = True
                    break
        return dp[-1]

# 140. Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wd = set(wordDict)
        store = {}
        
        def process(s):
            if s == '':
                return [[]]
            if s in store:
                return store[s]
            else:
                store[s] = []
            for i in range(1,len(s)+1):
                w = s[:i]
                if w in wd:
                    for sub in process(s[i:]):
                        store[s].append([w]+sub)
            return store[s]
        
        process(s)
        return [' '.join(wl) for wl in store[s]]

# 142. Linked List Cycle II
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        store = set()
        curr = head
        while curr is not None:
            if curr not in store:
                store.add(curr)
            else:
                return curr
            curr = curr.next
        return None
