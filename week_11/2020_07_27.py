# 1287. Element Appearing More Than 25% In Sorted Array
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) <= 3:
            return arr[0]
        
        window = len(arr)//4 + 1
        for i in range(len(arr)-window+1):
            if arr[i] == arr[i+window-1]:
                return arr[i]

# 1290. Convert Binary Number in a Linked List to Integer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return int(''.join(map(str, res)),2)

# 1295. Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        get_len = lambda x: 1 if len(str(x))%2==0 else 0
        lens = map(get_len, nums)
        return sum(lens)

# 1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        if len(arr) == 2:
            return [arr[-1], -1]
        
        right_max = [-1, arr[-1]]
        curr_max = max(arr[-1], arr[-2])
        for i in range(len(arr)-3, -1, -1):
            right_max.append(curr_max)
            curr_max = max(curr_max, arr[i])
        right_max.reverse()
        return right_max

# 1309. Decrypt String from Alphabet to Integer Mapping
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                digit = int(s[i:i+2])
                i += 3
            else:
                digit = int(s[i])
                i += 1
            base = ord('a')
            char = chr(base-1+digit)
            res += char
        return res
