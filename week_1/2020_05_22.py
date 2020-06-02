# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            start = ListNode(0)
            prev = start
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 if l1 is not None else l2
            return start.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            j = 1
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1]:
                    nums[j] = nums[i]
                    j = j+1
            return j

# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            j = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[j] = nums[i]
                    j = j + 1
            return j

# 28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_haystack = len(haystack)
        n_needle = len(needle)
        if n_needle == 0:
            return 0
        if n_haystack < n_needle:
            return -1
        
        for i in range(0, n_haystack-n_needle+1):
            if haystack[i:i+n_needle] == needle:
                return i
        
        return -1

# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target and i != len(nums)-1:
                if nums[i+1] > target:
                    return i+1
            if nums[i] < target and i == len(nums)-1:
                return i+1
            if nums[i] > target:
                return 0

class Solution:  # take the advantage of sorted array
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if target > nums[i]:
                i = i+1
            else:
                return i
        return i

# 38. Count and Say
class Solution:
    def get_next(self, s):
        num = s[0]
        count = 1
        i = 1
        say = ''
        while i < len(s):
            if s[i] == num:
                count += 1
            else:
                say = say+str(count)+str(num)
                num = s[i]
                count = 1
            i += 1
        say = say+str(count)+str(num)
        return say
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        while n > 1:
            n = n-1
            return self.get_next(self.countAndSay(n))

# 53. Maximum Subarray
class Solution: # divide and conqure
    def cross_sum(self, nums, left, right, middle):
        if left == right:
            return nums[left]
            
        left_cross_max = nums[middle]
        for i in range(middle-1, left-1, -1):
            rolling_sum = sum(nums[i:middle+1])
            left_cross_max = max(rolling_sum, left_cross_max)
            
        right_cross_max = nums[middle+1]
        for i in range(middle+2, right+1):
            rolling_sum = sum(nums[middle+1:i+1])
            right_cross_max = max(rolling_sum, right_cross_max)
            
        return left_cross_max+right_cross_max
        
    def divide_conquer(self, nums, left, right):
        if left == right:
            return nums[left]
            
        middle = (left+right)//2
            
        left_sum = self.divide_conquer(nums, left, middle)
        right_sum = self.divide_conquer(nums, middle+1, right)
        cross = self.cross_sum(nums, left, right, middle)
            
        return max(left_sum, right_sum, cross)
    
    
    def maxSubArray(self, nums: 'List[int]') -> 'int':      
        return self.divide_conquer(nums, 0, len(nums)-1)


class Solution: # dynamic programming
    def maxSubArray(self, nums: List[int]) -> int:
        overallmax = nums[0]
        max_contain_last_element = nums[0]
        for i in range(1,len(nums)):
            new_last_element = nums[i]
            max_contain_last_element = max(new_last_element, max_contain_last_element+new_last_element)
            overallmax = max(overallmax, max_contain_last_element)
        return overallmax

# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        return len(s.split(' ')[-1])

# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num + digits[i]*10**(len(digits)-i-1)
        newnum = num + 1
        newdigits = []
        while newnum > 0:
            newdigits.append(newnum%10)
            newnum = newnum // 10
        return newdigits[::-1]

# 67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) == 0:
            return a
        else:
            if a == '0':
                return b
            elif b == '0':
                return a
            else:
                maxlength = max(len(a),len(b))
                a, b = a.zfill(maxlength), b.zfill(maxlength)
                result = ''
                c = '0'
                map = {(0,0,0):(0,0), 
                       (0,0,1):(1,0), 
                       (0,1,0):(1,0), 
                       (0,1,1):(0,1), 
                       (1,0,0):(1,0),
                       (1,0,1):(0,1),
                       (1,1,0):(0,1),
                       (1,1,1):(1,1)}
                for i in range(-1, -maxlength-1, -1):
                    ai = int(a[i])
                    bi = int(b[i])
                    dig, push = map[(ai, bi, int(c))]
                    result = str(dig) + result
                    c = str(push)
                if c == '1':
                    result = c + result
                return result