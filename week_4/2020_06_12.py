# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = 0
        store = {}
        while head is not None:
            store[i] = head
            i += 1
            head = head.next
        mid = i//2
        return store[mid]
        
# 883. Projection Area of 3D Shapes
class Solution: 
    def projectionArea(self, grid: List[List[int]]) -> int:
        total = 0
        l = len(grid)
        w = len(grid[0])
        gridT = []
        for i in range(w):
            gridT.append([0]*l)
        count0 = 0
        for i in range(l):
            total += max(grid[i])
            for j in range(w):
                gridT[j][i] = grid[i][j]
                if grid[i][j] == 0:
                    count0 += 1
        total += (l*w-count0)
        for i in range(w):
            total += max(gridT[i])
        return total

# 884. Uncommon Words from Two Sentences
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = A.split()
        b = B.split()
        store = {}
        for w in a:
            if w in store:
                store[w][0] += 1
            else:
                store[w] = [1, 0]
        for w in b:
            if w in store:
                store[w][1] += 1
            else:
                store[w] = [0, 1]
        res = []
        for w in store:
            if store[w] == [1, 0] or store[w] == [0, 1]:
                res.append(w)
        return res

# 888. Fair Candy Swap
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a = sum(A)
        b = sum(B)
        diff = (b-a)/2
        setB = set(B) # use hashtable to speed up the following search
        for num in A:
            if num+diff in setB:
                return [num, num+diff]

# 892. Surface Area of 3D Shapes
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        l = len(grid)
        w = len(grid[0])
        for i in range(l):
            for j in range(w):
                side = grid[i][j]
                if side > 0:
                    total += 2
                    for nexti, nextj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if 0<=nexti<l and 0<=nextj<w:
                            nextval = grid[nexti][nextj]
                        else:
                            nextval = 0
                        total += max(side-nextval, 0)
        return total

# 893. Groups of Special-Equivalent Strings
class Solution: # slow
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def equal(s, t):
            odds = sorted(s[1:len(s):2])
            oddt = sorted(t[1:len(t):2])
            evens = sorted(s[::2])
            event = sorted(t[::2])
            return odds == oddt and evens == event
        
        store = set()
        store.add(A[0])
        for i in range(1,len(A)):
            if all(equal(w, A[i]) == False for w in store):
                store.add(A[i])
        return len(store)

class Solution: # a faster solution: the count of the even indexed letters in S, followed by the count of the odd indexed letters in S is a special tag for the group of equivalent words
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def special_tag(t):
            res = [0] * 52
            for i in range(len(t)):
                res[ord(t[i])-ord('a')+(i%2)*26] += 1
            return tuple(res)
        
        store = set()
        for w in A:
            store.add(special_tag(w))
        return len(store)

# 896. Monotonic Array
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A, reverse=True)

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i]<=A[i+1] for i in range(len(A)-1)) or all(A[i]>=A[i+1] for i in range(len(A)-1))

# 897. Increasing Order Search Tree
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res+inorder(root.right)
            return res
        
        res = inorder(root)
        tree = TreeNode(res[0])
        curr = tree
        for i in range(1,len(res)):
            node = TreeNode(res[i])
            curr.right = node
            curr = curr.right
        return tree

# 905. Sort Array By Parity
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: x%2)
        return A

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A)-1
        while r>l:
            if A[r] % 2 < A[l] % 2:
                A[l], A[r] = A[r], A[l]
            if A[l] % 2 == 0:
                l += 1
            if A[r] % 2 == 1:
                r -= 1
        
        return A

# 908. Smallest Range I
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_num = min(A)
        max_num = max(A)
        if max_num - min_num <= 2*K:
            return 0
        else:
            return max_num - min_num - 2*K

# 914. X of a Kind in a Deck of Cards
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        store = {}
        for num in deck:
            store[num] = 1 if num not in store else store[num]+1
        nums = set(store.values())
        min_num = min(nums)
        if min_num == 1:
            return False
        else:
            for x in range(2, min_num+1):
                if len(deck) % x == 0:
                    if all(v%x==0 for v in nums):
                        return True
            return False

# 917. Reverse Only Letters
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l = 0
        r = len(s)-1
        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l].isalpha() == False:
                l += 1
            if s[r].isalpha() == False:
                r -= 1
        return ''.join(s)

# 922. Sort Array By Parity II
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        res = []
        for num in A:
            if num%2 == 1:
                odd.append(num)
            else:
                even.append(num)
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        return res

class Solution: # transform in-place
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_position = 1
        for i in range(0,len(A),2):
            if A[i] % 2 == 1:
                while A[odd_position] % 2 == 1:
                    odd_position += 2
                A[i], A[odd_position] = A[odd_position], A[i]
        return A

# 925. Long Pressed Name
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        else:
            i = 0
            j = 0
            while i < len(name) and j < len(typed):
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                else:
                    if j == 0:
                        return False
                    elif typed[j] == typed[j-1]:
                        j += 1
                    else:
                        return False
            return {typed[j-1]} == set(typed[j-1:]) and i == len(name)

# 929. Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        def process(add):
            s = add.split('@')
            s[0] = s[0].replace('.','')
            if '+' in s[0]:
                index = s[0].index('+')
                s[0] = s[0][:index]
            return s[0]+'@'+s[1]
        
        store = set()
        for address in emails:
            store.add(process(address))
        return len(store)

# 933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        if self.queue == []:
            self.queue.append(t)
            return 1
        else:
            self.queue.append(t)
            while self.queue[0] < t - 3000:
                self.queue.pop(0)
            return len(self.queue)

# 937. Reorder Data in Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) <= 1:
            return logs
        else:
            letter_log = []
            digit_log = []
            for log in logs:
                index = log.index(' ')
                s = log[index+1:]
                if s[0].isalpha():
                    letter_log.append((s, log))
                else:
                    digit_log.append(log)
            letter_log.sort(key=lambda x: (x[0],x[1]))
            return [x[1] for x in letter_log] + digit_log

# 938. Range Sum of BST
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        def process(root):
            if root:
                if L<=root.val<=R:
                    self.total += root.val
                if L < root.val:
                    process(root.left)
                if R > root.val:
                    process(root.right)
        process(root)
        return self.total

# 941. Valid Mountain Array
# same as Q852
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 1
        while i < len(A) and A[i-1] < A[i]:
            i += 1
        
        if i == 1 or i == len(A):
            return False
        
        while i < len(A) and A[i-1] > A[i]:
            i += 1
        
        return i == len(A)

# 942. DI String Match
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low = 0
        high = len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        return res + [low]

# 944. Delete Columns to Make Sorted
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in range(len(A[0])):
            new = ''
            for w in A:
                new += w[i]
            if new != ''.join(sorted(new)):
                count += 1
        return count