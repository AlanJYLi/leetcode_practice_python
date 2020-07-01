# 173. Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res+inorder(root.right)
            return res
        
        self.sort = inorder(root)
        self.index = -1
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.sort[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index+1 < len(self.sort)

class BSTIterator: # to achieve O(h) space complexity (h is the height of the tree)

    def __init__(self, root: TreeNode):
        self.stack = []
        self.traverse_left(root)
    
    def traverse_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp = self.stack.pop()
        if temp.right is not None:
            self.traverse_left(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# 174. Dungeon Game
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        mark = [[0]*n for i in range(m)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    mark[i][j] = max(1, 1-dungeon[i][j])
                elif i == m-1 and j<n-1:
                    mark[i][j] = max(1, mark[i][j+1]-dungeon[i][j])
                elif i < m-1 and j == n-1:
                    mark[i][j] = max(1, mark[i+1][j]-dungeon[i][j])
                else:
                    mark[i][j] = min(max(1, mark[i+1][j]-dungeon[i][j]), max(1, mark[i][j+1]-dungeon[i][j]))
        return mark[0][0]

# 179. Largest Number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ''
        if len(nums) == 1:
            return str(nums[0])
        
        max_l = 0
        for n in nums:
            max_l = max(max_l, len(str(n)))
        
        temp = []
        for n in nums:
            s = str(n)
            new1 = s + s[0]*(max_l-len(s))
            new2 = s + s[-1]*(max_l-len(s))
            temp.append([int(new1),int(new2),n])
        
        temp = sorted(temp, key = lambda x: (x[0],x[1]), reverse=True)
        s = ''
        for a,b,c in temp:
            s += str(c)
        
        if all(x=='0' for x in s):
            return '0'
        else:
            return s

# 186. Reverse Words in a String II
class Solution: # in-place: reverse the whole list and then reverse each word
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        i = 0
        j = 0
        while i < len(s):
            while j < len(s):
                if s[j] != ' ':
                    j += 1
                else:
                    break
            l = i
            r = j-1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i = j+1
            j = i

# 187. Repeated DNA Sequences
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in seen:
                res.add(sub)
            else:
                seen.add(sub)
        return list(res)
