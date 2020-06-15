# 2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res =ListNode(-1)
        curr = res
        curr1 = l1
        curr2 = l2
        addone = 0
        while curr1 is not None or curr2 is not None or addone > 0:
            if curr1 is None:
                x = 0
            else:
                x = curr1.val
                curr1 = curr1.next
            if curr2 is None:
                y = 0
            else:
                y = curr2.val
                curr2 = curr2.next
            total = x + y + addone
            digit = total % 10
            addone = total // 10
            newnode = ListNode(digit)
            curr.next = newnode
            curr = curr.next
        return res.next

# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        else:
            queue = [s[0]]
            seen = {s[0]}
            res = 0
            for i in range(1,len(s)):
                if s[i] not in seen:
                    queue.append(s[i])
                    seen.add(s[i])
                else:
                    res = max(res, len(queue))
                    while queue[0] != s[i]:
                        go = queue.pop(0)
                        seen.remove(go)
                    queue.pop(0)
                    queue.append(s[i])
            return max(res, len(queue))

class Solution: # faster: sliding window; when finding a duplicate in the range [i, j) with index m, skip all the elements in the range [i, m], and let i = m+1.
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        else:
            i = 0
            res = 0
            store = {}
            for j, letter in enumerate(s):
                if letter in store and i <= store[letter]:
                    res = max(res, j-i)
                    i = store[letter] + 1
                store[letter] = j
            return max(res, j-i+1)

# 4. Median of Two Sorted Arrays
class Solution: # time complexity: (m+n)/2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = (len(nums1)+len(nums2)-1) // 2
        index2 = (len(nums1)+len(nums2)) // 2
        if nums1 == [] and nums2 != []:
            return (nums2[index1]+nums2[index2])/2
        elif nums1 != [] and nums2 == []:
            return (nums1[index1]+nums1[index2])/2
        else:
            store = []
            i = 0
            j = 0    
            while (len(store) < max(index1, index2) + 1) and (i < len(nums1) or j < len(nums2)):
                if i < len(nums1) and j < len(nums2):
                    if nums1[i] == nums2[j]:
                        store.append(nums1[i])
                        store.append(nums2[j])
                        i += 1
                        j += 1
                    elif nums1[i] > nums2[j]:
                        store.append(nums2[j])
                        j += 1
                    else:
                        store.append(nums1[i])
                        i += 1
                elif i == len(nums1) and j < len(nums2):
                    store.append(nums2[j])
                    j += 1
                elif i < len(nums1) and j == len(nums2):
                    store.append(nums1[i])
                    i += 1

class Solution: # time complexity: log(min(m,n))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        if a == 0 and b > 0:
            return (nums2[(b-1)//2]+nums2[b//2])/2
        if b == 0 and a > 0:
            return (nums1[(a-1)//2]+nums1[a//2])/2
        
        if a > b:
            nums1, nums2, a, b = nums2, nums1, b, a
        half = (a+b+1) // 2
        l = 0
        r = a
        while l <= r:
            i = (l+r) // 2
            j = half - (i + 1)
            if i < a and nums2[j] > nums1[i]:
                l = i+1
            elif i > 0 and nums1[i-1] > nums2[j+1]:
                r = i-1
            else:
                if i == 0:
                    mid_left = nums2[j]
                elif j == -1:
                    mid_left = nums1[i-1]
                else:
                    mid_left = max(nums2[j], nums1[i-1])
                
                if (a+b)%2 == 1:
                    return mid_left
                
                if i == a:
                    mid_right = nums2[j+1]
                elif j == b-1:
                    mid_right = nums1[i]
                else:
                    mid_right = min(nums2[j+1], nums1[i])
                return (mid_left+mid_right)/2

# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def centerexpand(s, L, R): # palindromic string is symmetrical around its center; for a center, return the length of palindromic string
            l = L
            r = R
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r-l-1
        
        if len(s) <= 1:
            return s
        else:
            left = 0
            right = 0
            for i in range(len(s)):
                len1 = centerexpand(s, i, i) # iterate among all centers
                len2 = centerexpand(s, i, i+1)
                res = max(len1, len2)
                if res > right-left:
                    left = i - (res-1) // 2
                    right = i + res // 2
            return s[left:right+1]

# 6. ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        d = numRows + numRows - 2
        res = ''
        for i in range(numRows):
            for j in range(i, len(s), d):
                res = res + s[j]
                if j < j+d-2*i < j+d and j+d-2*i < len(s):
                    res = res + s[j+d-2*i]
        return res

# 8. String to Integer (atoi)
class Solution:
    def myAtoi(self, str: str) -> int:
        a = str.strip()
        if a == '':
            return 0
        elif len(a) == 1:
            if a[0].isdigit():
                return int(a)
            else:
                return 0
        else:
            if a[0].isalpha():
                return 0
            elif a[0] == '-':
                sign = -1
                a = a[1:]
            elif a[0] == '+':
                sign = 1
                a = a[1:]
            elif a[0].isdigit():
                sign = 1
            
            if a[0].isdigit() == False: # case: '++23' -> '+23', '-a32' -> 'a32'
                return 0
            else:
                if a[0] == '0': # case: '000123'
                    j = 1
                    while j < len(a):
                        if a[j] == '0':
                            j += 1
                        else:
                            break
                    if j == len(a):
                        return 0
                    a = a[j:]
                for i in range(len(a)):
                    if a[i].isdigit() == False:
                        a = a[:i]
                        break
                if len(a) == 0:
                    return 0
            int_min = ''
            int_max = ''
            num1 = 2**31
            num2 = 2**31-1
            base = ord('0')
            while num1 > 0:
                int_min = chr((num1%10)+base) + int_min
                num1 = num1//10
                int_max = chr((num2%10)+base) + int_max
                num2 = num2//10
            if len(a) < len(int_min):
                return int(a)*sign
            elif len(a) > len(int_min):
                return -2**31 if sign == -1 else 2**31-1
            else:
                i = 0
                while  i < len(a)-1:
                    if a[i] > int_min[i]:
                        return -2**31 if sign == -1 else 2**31-1
                    elif a[i] < int_min[i]:
                        return int(a)*sign
                    else:
                        i += 1
                if sign == -1 and int(a[-1]) >= int(int_min[-1]):
                    return -2**31
                elif sign == -1 and int(a[-1]) < int(int_min[-1]):
                    return int(a)*sign
                elif sign == 1 and int(a[-1]) >= int(int_max[-1]):
                    return 2**31-1
                elif sign == 1 and int(a[-1]) < int(int_max[-1]):
                    return int(a)

# 10. Regular Expression Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        elif s != '' and p == '':
            return False
        else:
            match = bool(s) and p[0] in {s[0], '.'}
            if len(p) >= 2 and p[1] == '*':
                return (self.isMatch(s, p[2:])) or (match and self.isMatch(s[1:], p))
            else:
                return match and self.isMatch(s[1:], p[1:])

class Solution: # similar as approach above, but save the results of whether s[i:] and p[j:] match. It's faster because it saves expensive string-building operations
    def isMatch(self, s: str, p: str) -> bool:
        store = {}
        def process(i, j):
            if (i, j) not in store:
                if j == len(p):
                    res = i == len(s)
                else:
                    match = i < len(s) and p[j] in {'.', s[i]}
                    if j+1 < len(p) and p[j+1] == '*':
                        res = process(i, j+2) or (match and process(i+1, j))
                    else:
                        res = match and process(i+1, j+1)
                store[(i,j)] = res
            return store[(i,j)]
        
        return process(0,0)

# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        if num > 0:
            thousand, num = num // 1000, num % 1000
            res += 'M' * thousand
            
        if num > 0:
            hundred, num = num // 100, num % 100
            if hundred == 9:
                res += 'CM'
            elif hundred >= 5:
                res += 'D' + 'C'*(hundred-5)
            elif hundred == 4:
                res += 'CD'
            else:
                res += 'C' * hundred
                
        if num > 0:
            tenth, num = num // 10, num % 10
            if tenth == 9:
                res += 'XC'
            elif tenth >= 5:
                res += 'L' + 'X'*(tenth-5)
            elif tenth == 4:
                res += 'XL'
            else:
                res += 'X' * tenth
        
        if num > 0:
            if num == 9:
                res += 'IX'
            elif num >= 5:
                res += 'V' + 'I'*(num-5)
            elif num == 4:
                res += 'IV'
            else:
                res += 'I' * num
        
        return res

# 15. 3Sum
class Solution: # target + two sum (use two pointer on sorted list to solve two sum)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(s, target):
            res = set()
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] + s[r] < target:
                    l += 1
                elif s[l] + s[r] > target:
                    r -= 1
                else:
                    res.add((s[l], s[r]))
                    l += 1
                    r -= 1
            return res
        
        res = []
        a = sorted(nums)
        seen = set()
        for i in range(len(a)-2):
            if a[i] > 0:
                break
            else:
                if a[i] not in seen:
                    seen.add(a[i])
                    two = twoSum(a[i+1:], -a[i])
                    if len(two) > 0:
                        for n1, n2 in two:
                            res.append([a[i], n1, n2])
        return res

# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        def closeTwoSum(s, num, target):
            l = 0
            r = len(s)-1
            diff = float('inf')
            while l < r:
                total = num+s[l]+s[r]
                if abs(target-total) < abs(diff):
                    diff = target-total
                if diff == 0:
                    break
                if total < target:
                    l += 1
                else:
                    r -= 1
            return target-diff
                          
        a = sorted(nums)
        best = float('inf')
        res = 0
        for i in range(len(a)-2):
            total = closeTwoSum(a[i+1:], a[i], target)
            if total == target:
                res = total
                break
            if abs(total-target) < best:
                best = abs(total-target)
                res = total
        return res
