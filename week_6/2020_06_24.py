# 97. Interleaving String
class Solution: # exceed time limit
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def process(s1, i, s2, j, res, s3):
            if res == s3 and i == len(s1) and j == len(s2):
                return True
            
            mark = False
            if i < len(s1):
                mark = mark or process(s1,i+1,s2,j,res+s1[i],s3)
            if j < len(s2):
                mark = mark or process(s1,i,s2,j+1,res+s2[j],s3)
            return mark
        
        return process(s1,0,s2,0,'',s3)
 
 class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        store = {}
        
        def process(s1, i, s2, j, s3, k):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if (i,j) in store:
                return store[(i,j)]
            mark = False
            if (s1[i] == s3[k] and process(s1,i+1,s2,j,s3,k+1)) or (s2[j] == s3[k] and process(s1,i,s2,j+1,s3,k+1)):
                mark = True
            store[(i,j)] = mark
            return mark
        
        return process(s1,0,s2,0,s3,0)           

# 98. Validate Binary Search Tree
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res + inorder(root.right)
            return res
        
        res = inorder(root)
        return all(res[i-1]<res[i] for i in range(1,len(res)))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        stack = []
        prev = None
        curr = root
        while curr is not None or len(stack)>0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is None:
                prev = curr.val
            else:
                if prev >= curr.val:
                    return False
                else:
                    prev = curr.val
            curr = curr.right
        return True

# 99. Recover Binary Search Tree
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res+inorder(root.right)
            return res
        
        # find the swapped values
        res = inorder(root)
        x = None
        y = None
        for i in range(len(res)-1):
            if res[i+1]<res[i]:
                y = res[i+1]
                if x is None:
                    x = res[i]
                else:
                    break
        
        stack = [root]
        x_done = False
        y_done = False
        while len(stack) > 0:
            curr = stack.pop()
            if x_done == True and y_done == True:
                break
            elif x_done == False and curr.val == x:
                curr.val = y
                x_done = True
            elif y_done == False and curr.val == y:
                curr.val = x
                y_done = True
            
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        prev = None
        curr = root
        x = None
        y = None
        while curr is not None or len(stack)>0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is not None and curr.val < prev.val:
                y = curr
                if x is None:
                    x = prev
                else:
                    break
            prev = curr
            curr = curr.right
        
        x.val, y.val = y.val, x.val

# 102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        while len(queue) > 0:
            n = len(queue)
            level = []
            for i in range(n):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            res.append(level)
        return res

# 103. Binary Tree Zigzag Level Order Traversal
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        res = []
        level = 0
        while len(queue) > 0:
            n = len(queue)
            ele = []
            for i in range(n):
                curr = queue.pop(0)
                ele.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            if level % 2 == 0:
                res.append(ele)
            else:
                res.append(ele[::-1])
            level += 1
        return res

# 105. Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        
        self.pre = 0
        
        def process(l, r):
            if l == r:
                return None
            val = preorder[self.pre]
            root = TreeNode(val)
            i = index[val]
            
            self.pre += 1
            root.left = process(l, i)
            root.right = process(i+1,r)
            return root
        
        return process(0, len(inorder))

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        
        stack = []
        root = None
        for v in preorder:
            if root is None:
                root = TreeNode(v)
                stack.append(root)
            else:
                new = TreeNode(v)
                if index[v] < index[stack[-1].val]:
                    stack[-1].left = new
                else:
                    while len(stack) > 0 and index[stack[-1].val] < index[v]:
                        curr = stack.pop()
                    curr.right = new
                stack.append(new)
        return root

# 106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        
        self.pre = -1
        
        def process(l, r):
            if l == r:
                return None
            val = postorder[self.pre]
            root = TreeNode(val)
            i = index[val]
            
            self.pre -= 1
            root.right = process(i+1, r)
            root.left = process(l,i)
            return root
        
        return process(0, len(inorder))

# 109. Convert Sorted List to Binary Search Tree
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        
        def process(l,r):
            if l > r:
                return None
            
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = process(l, mid-1)
            root.right = process(mid+1, r)
            return root
        
        return process(0,len(nums)-1)
