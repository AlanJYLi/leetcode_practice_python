# 17. Letter Combinations of a Phone Number
class Solution: # similar with Q784
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                   '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                   '8':['t','u','v'], '9':['w','x','y','z']}
        res = []
        for d in digits:
            if res == []:
                for s in mapping[d]:
                    res.append([s])
            else:
                n = len(res)
                option = len(mapping[d])
                for i in range(n*(option-1)):
                    res.append(res[i][:])
                for j in range(option):
                    for i in range(n):
                        res[j*n+i].append(mapping[d][j])
        return [x for x in map(''.join, res)]

# 18. 4Sum
class Solution: # warp 3Sum
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(s, t):
            res = set()
            s = sorted(s)
            for i in range(len(s)-2):
                twosum = t-s[i]
                remain = s[i+1:]
                l = 0
                r = len(remain)-1
                while l < r:
                    if remain[l] + remain[r] == twosum:
                        res.add((s[i], remain[l], remain[r]))
                        l += 1
                        r -= 1
                    elif remain[l] + remain[r] < twosum:
                        l += 1
                    else:
                        r -= 1
            return res
        
        a = sorted(nums)
        res = set()
        for i in range(len(a)-3):
            t = target - a[i]
            s = a[i+1:]
            qua = threeSum(s, t)
            if len(qua) > 0:
                for x,y,z in qua:
                    res.add((a[i],x,y,z))
        return [x for x in map(list, res)]

class Solution: # a general kSum approach: recursion. Faster than above
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def twoSum(nums, target):
            res = set()
            l = 0
            r = len(nums)-1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.add((nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
            return [x for x in map(list, res)]
        
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0]*k>target or nums[-1]*k<target:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    s = kSum(nums[i+1:], target-nums[i], k-1)
                    for set in s:
                        res.append([nums[i]]+set)
            return res
        
        a = sorted(nums)
        return kSum(a, target, 4)

# 19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        probe = ListNode(0, head) # add a dummy head to simplify some edge cases (e.g only one node; remove the first node)
        gofirst = probe
        gosecond = probe
        for i in range(n):
            gofirst = gofirst.next
        while gofirst.next is not None:
            gofirst = gofirst.next
            gosecond = gosecond.next
        gosecond.next = gosecond.next.next
        return probe.next

# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def process(s, left, right):
            if len(s) == 2*n:
                res.append(s)
            if left > 0:
                process(s+'(', left-1, right)
            if left < right:
                process(s+')', left, right-1)
        
        process('',n , n)
        return res

# 23. Merge k Sorted Lists
class Solution: # brute force
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for l in lists:
            while l is not None:
                nodes.append(l.val)
                l = l.next
        head = ListNode(0)
        curr = head
        for num in sorted(nodes):
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

class Solution: # compare one by one
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return None
        head = ListNode(0)
        curr = head
        pool = []
        for l in lists:
            if l is not None:
                pool.append((l.val,l))
        pool.sort(key=lambda x: x[0])
        while len(pool) > 0:
            val, node = pool.pop(0)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next is not None:
                pool.append((node.next.val, node.next))
                pool.sort(key=lambda x: x[0])
        return head.next

class Solution: # Merge with Divide And Conquer: iterately merge two linked lists
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwo(l1, l2):
            head = ListNode(0)
            curr = head
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                curr = curr.next
            if l1 is None:
                curr.next = l2
            elif l2 is None:
                curr.next = l1
            return head.next    
        
        n = len(lists)
        if n == 0:
            return None
        store = []
        for i in range(0, n, 2):
            if i+1 < n:
                store.append(mergeTwo(lists[i], lists[i+1]))
            else:
                store.append(lists[i])
        while len(store) > 1:
            lists = store
            store = []
            n = len(lists)
            for i in range(0, n, 2):
                if i+1 < n:
                    store.append(mergeTwo(lists[i], lists[i+1]))
                else:
                    store.append(lists[i])
        
        return store[0]

# 24. Swap Nodes in Pairs
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next is not None:
            n1 = curr.next
            n2 = curr.next.next
            if n2 is not None:
                curr.next = n2
                n1.next = n2.next
                n2.next = n1
                curr = curr.next.next
            else:
                break
        return dummy.next

class Solution: # recursion
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        n1 = head
        n2 = head.next
        n1.next = self.swapPairs(n2.next)
        n2.next = n1
        
        return n2

# 25. Reverse Nodes in k-Group
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLinkedList(head, k):
            new = None
            curr = head
            while k > 0:
                nextnode = curr.next
                curr.next = new
                new = curr
                curr = nextnode
                k -= 1
            return new
               
        count = 0
        curr = head
        while count < k and curr is not None:
            curr = curr.next
            count += 1
        
        if count == k:
            reverselink = reverseLinkedList(head, k)
            head.next = self.reverseKGroup(curr, k)
            return reverselink
        
        return head

# 29. Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        HALF_MIN_INT = -1073741824
        if dividend == 0:
            return 0
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        
        # change to negative number to avoid overflow
        if dividend > 0 and divisor > 0:
            sign = 1
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0 and divisor > 0:
            sign = -1
            divisor = -divisor
        elif dividend > 0 and divisor < 0:
            sign = -1
            dividend = -dividend
        else:
            sign = 1
        
        res = 0
        while divisor >= dividend:
            power = 1
            val = divisor
            while val >= HALF_MIN_INT and val+val >= dividend:
                val = val + val
                power = power + power
            res += power
            dividend -=val
        return res if sign == 1 else -res

class Solution: # similar as above, but only compute the exponential sequence just once
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        HALF_MIN_INT = -1073741824
        if dividend == 0:
            return 0
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        
        # change to negative number to avoid overflow
        if dividend > 0 and divisor > 0:
            sign = 1
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0 and divisor > 0:
            sign = -1
            divisor = -divisor
        elif dividend > 0 and divisor < 0:
            sign = -1
            dividend = -dividend
        else:
            sign = 1
        
        powers = []
        nums = []
        power = 1
        val = divisor
        while val >= dividend:
            powers.append(power)
            nums.append(val)
            if val < HALF_MIN_INT:
                break
            power += power
            val += val
            
        
        res = 0
        for i in range(-1, -len(powers)-1, -1):
            if nums[i] >= dividend:
                res += powers[i]
                dividend -= nums[i]
        
        return res if sign==1 else -res