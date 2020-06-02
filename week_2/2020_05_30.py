# 258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            total = 0
            while num > 0:
                remain = num % 10
                num = num // 10
                total += remain
            if total < 10:
                return total
            else:
                num = total

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

# 263. Ugly Number
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        elif num == 2 or num == 3 or num == 5:
            return True
        else:
            if num % 2 == 0:
                return self.isUgly(num//2)
            elif num % 3 == 0:
                return self.isUgly(num//3)
            elif num % 5 == 0:
                return self.isUgly(num//5)
            else:
                return False

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        
        factor = [2,3,5]
        
        for p in factor:
            while num % p == 0:
                num = num // p
        
        return num == 1

# 266. Palindrome Permutation
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        store = {}
        for l in s:
            if l not in store:
                store[l] = 1
            else:
                if store[l] == 1:
                    store[l] = 0
                else:
                    store[l] = 1
        print(store)
        return sum(store.values()) == 0 or sum(store.values()) == 1

# 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n+0)*(n+1)//2 - sum(nums)

# 270. Closest Binary Search Tree Value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res + inorder(root.right)
            return res
            
        sortedlist = inorder(root)
        if target <= sortedlist[0]:
            return sortedlist[0]
        if target >= sortedlist[-1]:
            return sortedlist[-1]
        
        l = 0
        r = len(sortedlist)
        while r-l > 1:
            mid = sortedlist[(l+r)//2]
            if mid == target:
                return mid
            elif mid < target:
                l = (l+r)//2
            else:
                r = (l+r)//2
        return sortedlist[l] if target-sortedlist[l]<=sortedlist[r]-target else sortedlist[r]

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        close = root.val
        while root is not None:
            close = root.val if abs(root.val-target)<=abs(close-target) else close
            root = root.left if target < root.val else root.right
        return close