# 171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            letter = s[i]
            power = len(s) - i - 1
            sum = sum + 26**power*(ord(letter)-ord('A')+1)
        return sum

# 172. Factorial Trailing Zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        count = 0
        divide = 5
        
        while n >= divide:
            count = count + n // divide
            divide = divide * 5
        
        return count

# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        start = 0
        count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_index = (current+k)%n
                nums[next_index], prev = prev, nums[next_index]
                current = next_index
                count = count+1
                
                if start == current:
                    break
            
            start = start+1

# 190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        store = ''
        while n > 0:
            remain = n % 2
            n = n // 2
            store = str(remain) + store
        
        if len(store) < 32:
            store = '0' * (32-len(store)) + store
        
        store = store[::-1]
        
        new_num = 0
        for i in range(32):
            new_num = new_num + int(store[i]) * 2**(32-i-1)
        
        return new_num

# 191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            remain = n % 2
            n = n // 2
            if remain == 1:
                count += 1
        return count

# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <=2:
            return max(nums)
        else:
            lag_2_best = nums[0]
            lag_1_best = max(nums[0:2])
            overall = max(lag_2_best, lag_1_best)
            
            for i in range(2, len(nums)):
                new_house = nums[i]
                current = lag_2_best + new_house
                lag_2_best = overall
                overall = max(current, lag_1_best, overall)
                lag_1_best = current
            
            return overall

class Solution:
    def rob(self, nums: List[int]) -> int:
        prevmax = 0
        currentmax = 0
        for n in nums:
            temp = currentmax
            currentmax = max(prevmax+n,currentmax)
            prevmax = temp
        return currentmax

# 202. Happy Number
class Solution:
    
    def beforehappy(self, n):
        if n == 0:
            return False
        
        while n > 10:
            if n // 10 == 0:
                n = n / 10
            else:
                return False
        
        if n == 1:
            return True
        else:
            return False
    
    def isHappy(self, n: int) -> bool:
        store = {}
        while self.beforehappy(n) == False:
            new_n = 0
            while n > 0:
                remain = n % 10
                n = n // 10
                new_n += remain**2
            n = new_n
            if n in store:
                return False
            else:
                store[n] = 1
        
        return True

# 203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # add a node prior to the linked list can make it easy to deal with the issue when the target value is at the head of the linked list
        newstart = ListNode(0)
        newstart.next = head
        
        prev = newstart
        curr = head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return newstart.next

# 204. Count Primes
class Solution: # Sieve algorithm
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        sqrt = int(n**0.5)
        
        mark = [1] * n
        mark[0] = 0
        mark[1] = 0
        
        for i in range(2, sqrt+1):
            if mark[i] == 1:
                for j in range(i**2, n, i):
                    mark[j] = 0
            else:
                continue
                
        return sum(mark)

# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lettermap = {}
        alreadymapped = {}
        for i in range(len(s)):
            s_letter = s[i]
            t_letter = t[i]
            if s_letter not in lettermap:
                lettermap[s_letter] = t_letter
                if t_letter in alreadymapped:
                    return False
                else:
                    alreadymapped[t_letter] = 0
            else:
                if lettermap[s_letter] != t_letter:
                    return False
                else:
                    continue
        return True

# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new = ListNode(head.val)
        rest = head.next
        
        while rest is not None:
            new = ListNode(rest.val, new)
            rest = rest.next
        
        return new

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for n in nums:
            if n not in store:
                store[n] = 1
            else:
                return True
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in store:
                diff = i - store[n]
                if diff <= k:
                    return True
            store[n] = i
        return False