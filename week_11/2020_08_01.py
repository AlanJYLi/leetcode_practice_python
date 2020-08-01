# 1450. Number of Students Doing Homework at a Given Time
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count

# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            w = sentence[i]
            if w.startswith(searchWord):
                return i+1
        return -1

# 1460. Make Two Arrays Equal by Reversing Sub-arrays
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d_target = {}
        d_arr = {}
        for num in target:
            d_target[num] = 1 if num not in d_target else 1+d_target[num]
        for num in arr:
            d_arr[num] = 1 if num not in d_arr else 1+d_arr[num]
        return d_target==d_arr

# 1464. Maximum Product of Two Elements in an Array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[0]-1)*(nums[1]-1), (nums[-1]-1)*(nums[-2]-1))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1 = max(nums[0], nums[1])
        max_2 = min(nums[0], nums[1])
        min_1 = min(nums[0], nums[1])
        min_2 = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            val = nums[i]
            if val <= max_2:
                continue
            elif val > max_2 and val <= max_1:
                max_2 = val
            else:
                max_2 = max_1
                max_1 = val
            if val >= min_2:
                continue
            elif val < min_2 and val >= min_1:
                min_2 = val
            else:
                min_2 = min_1
                min_1 = val
        return max((max_1-1)*(max_2-1), (min_1-1)*(min_2-1))

# 1469. Find All The Lonely Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        
        if root is None:
            return res
        
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if curr.left is not None and curr.right is not None:
                stack.append(curr.left)
                stack.append(curr.right)
            elif curr.left is None and curr.right is not None:
                res.append(curr.right.val)
                stack.append(curr.right)
            elif curr.left is not None and curr.right is None:
                res.append(curr.left.val)
                stack.append(curr.left)
        return res
