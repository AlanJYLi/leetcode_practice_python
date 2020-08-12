# 320. Generalized Abbreviation
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(idx, curr, word):
            if idx == len(word):
                res.append(curr)
                return
            
            backtrack(idx+1, curr+word[idx], word)
            for i in range(1, len(word)+1-idx):
                if curr == '' or curr[-1].isdigit() == False:
                    backtrack(idx+i, curr+str(i), word)
                else:
                    return
        
        res = []
        backtrack(0,'', word)
        return res

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(word, curr):
            if word == '':
                res.append(curr)
            for i in range(1, len(word)+1):
                if curr == '' or curr[-1].isalpha():
                    dfs(word[i:], curr+str(i))
                if curr == '' or curr[-1].isdigit():
                    dfs(word[i:], curr+word[:i])
        
        res = []
        dfs(word, '')
        return res

# 322. Coin Change
class Solution: # exceed time limit
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        
        store = {}
        minval = min(coins)
        coins = set(coins)
        for i in range(minval, amount+1):
            if i in coins:
                store[i] = 1
            else:
                j = 1
                store[i] = -1
                while j <= i//2:
                    if j in store and i-j in store and store[j] != -1 and store[i-j] != -1:
                        if store[i] == -1:
                            store[i] = store[j]+store[i-j]
                        else:
                            store[i] = min(store[i], store[j]+store[i-j])
                    j += 1
        return store[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        store = {0:0}
        for i in range(1, amount+1):
            store[i] = float('inf')
        
        for c in coins:
            for i in range(c, amount+1):
                store[i] = min(store[i], store[i-c]+1)
        
        return store[amount] if store[amount] != float('inf') else -1

# 323. Number of Connected Components in an Undirected Graph
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        store = {}
        for i in range(n):
            store[i] = set()
        for n1, n2 in edges:
            store[n1].add(n2)
            store[n2].add(n1)
        
        def dfs(node, seen):
            seen.add(node)
            for adj in store[node]:
                if adj not in seen:
                    dfs(adj, seen)
        
        count = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                dfs(node, seen)
                count += 1
        return count

# 325. Maximum Size Subarray Sum Equals k
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        store = {0:0}
        total = 0
        res = 0
        for i, val in enumerate(nums):
            total += val
            if total not in store:
                store[total] = i
            if total == k:
                res = max(res, i+1)
            if total-k in store:
                res = max(res, i-store[total-k])
        return res if res != len(nums)+1 else 0

# 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        even = head
        odd = head.next
        odd_curr = head.next
        while odd_curr is not None and odd_curr.next is not None:
            even.next = odd_curr.next
            even = even.next
            odd_curr.next = even.next
            odd_curr = odd_curr.next
        even.next = odd
        return head
