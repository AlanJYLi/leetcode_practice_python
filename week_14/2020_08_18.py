# 369. Plus One Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        num = 0
        curr = head
        while curr is not None:
            num = num*10 + curr.val
            curr = curr.next
        num += 1
        curr = None
        while num > 0:
            res = ListNode(num%10, curr)
            num = num//10
            curr = res
        return res

# 370. Range Addition
class Solution: # exceed time limit
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for a, b, t in updates:
            for i in range(a,b+1):
                res[i] += t
        return res

class Solution: # cumsum
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length+1)
        for s, e, val in updates:
            res[s] += val
            res[e+1] -= val
        for i in range(1, len(res)):
            res[i] = res[i] + res[i-1]
        return res[:-1]

# 376. Wiggle Subsequence
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [0] * len(nums)
        down = [0] * len(nums)
        if len(nums) == 0:
            return 0
        
        up[0] = 1
        down[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(up[-1], down[-1])

