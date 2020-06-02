# 100. Same Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 101. Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # recursion
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def compare(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
                return False
            
            if root1.val != root2.val:
                return False
            
            return compare(root1.left, root2.right) and compare(root1.right, root2.left)
        
        if root is None:
            return True
        
        return compare(root.left, root.right)

class Solution: # iteration
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while len(queue) > 0:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 is None and t2 is None:
                continue
            if (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

# 104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        stack = [(1, root)]
        
        maxdepth = 0
        while len(stack) > 0:
            curr_depth, curr = stack.pop()
            maxdepth = max(curr_depth, maxdepth)
            if curr.left is not None:
                stack.append((curr_depth+1, curr.left))
            if curr.right is not None:
                stack.append((curr_depth+1, curr.right))
        return maxdepth

# 107. Binary Tree Level Order Traversal II
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        
        while len(queue) > 0:
            num_nodes = len(queue)
            level = []
            while num_nodes > 0:
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                num_nodes -= 1
            res.append(level)
        
        return res[::-1]

# 108. Convert Sorted Array to Binary Search Tree
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        
        while len(nums) > 1:
            mid = len(nums) // 2
            
            val = nums[mid]
            left_part = nums[:mid]
            right_part = nums[mid+1:]
            
            return TreeNode(val, self.sortedArrayToBST(left_part), self.sortedArrayToBST(right_part))

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(left,right):
            if left > right:
                return None
            
            mid = (left+right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid+1, right)
            return root
        
        return build(0,len(nums)-1)