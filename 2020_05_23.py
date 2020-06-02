# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        else:
            l, h = 1, x
            while l <= h:
                mid = (l+h) // 2
                if mid**2 == x:
                    return mid
                elif mid**2 > x:
                    h = mid-1
                else:
                    l = mid +1
            return h

# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        map = {1:1, 2:2}
        for i in range(3,n+1):
            map[i] = map[i-1] + map[i-2]
        return map[n]

# 83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        prev = head
        curr = head.next
        
        while curr is not None:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        
        return head

# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for num in nums2:
            while i < m:
                if num > nums1[i]:
                    i += 1
                else:
                    for j in range(m, i, -1):
                        nums1[j] = nums1[j-1]
                    nums1[i] = num
                    m = m+1
                    break
            
            if i == m:
                nums1[m] = num
                m = m+1

