# 331. Verify Preorder Serialization of a Binary Tree
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        space = 1
        for c in preorder.split(','):
            space -= 1
            if space < 0:
                return False
            if c != '#':
                space += 2
        return space == 0

# 333. Largest BST Subtree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0
        
        def process(root):
            if root is None:
                return 0, float(inf), float(-inf)
            left, leftmin, leftmax = process(root.left)
            right, rightmin, rightmax = process(root.right)
            if leftmax < root.val < rightmin:
                self.res = left + right + 1
                return self.res, min(root.val, leftmin), max(root.val, rightmax)
            else:
                self.res = max(left, right)
                return self.res, float(-inf), float(inf)
            
        process(root)
        return self.res

# 334. Increasing Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        
        best = [float(inf), float(inf)]
        for i in range(len(nums)):
            v = nums[i]
            if v <= best[0]:
                best[0] = v
            elif v > best[0] and v <= best[1]:
                best[1] = v
            else:
                return True
        return False

# 337. House Robber III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def process(root): # return (value when robbing this node, value when not robbing this node)
            if root is None:
                return 0, 0
            
            takeleft, nottakeleft = process(root.left)
            takeright, nottakeright = process(root.right)
            return root.val+nottakeleft+nottakeright, max(takeleft, nottakeleft)+max(takeright, nottakeright)
        
        return max(process(root))

# 338. Counting Bits
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        for i in range(1, len(res)):
            res[i] = res[((i-1) & i)] + 1
        return res
