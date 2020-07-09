# 224. Basic Calculator
class Solution:
    def calculate(self, s: str) -> int:
        
        def simple_expression(s):
            res = 0
            sign = 1
            i = 0
            while i < len(s):
                if s[i] == '-':
                    sign = -1
                    i += 1
                    if i < len(s) and s[i].isdigit() == False:
                        sign = -1 if s[i] == '+' else 1
                        i += 1
                elif s[i] == '+':
                    sign = 1
                    i += 1
                    if i < len(s) and s[i].isdigit() == False:
                        sign = -1 if s[i] == '-' else 1
                        i += 1
                elif s[i].isdigit():
                    val = s[i]
                    j = i+1
                    while j < len(s) and s[j].isdigit():
                        val += s[j]
                        j += 1
                    i = j
                    res += int(val)*sign
            return res
               
        stack = []
        for l in s:
            if l == ' ':
                continue
            elif l == ')':
                exp = ''
                element = stack.pop()
                while element != '(':
                    exp = element+exp
                    element = stack.pop()
                stack.append(str(simple_expression(exp)))
            else:
                stack.append(l)
        exp = ''.join(stack)
        return simple_expression(exp)

# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            left = nums[i]
            j = i+1
            while j < len(nums) and nums[j] == nums[j-1]+1:
                j += 1
            right = nums[j-1]
            if left == right:
                res.append(str(left))
            else:
                res.append(str(left)+'->'+str(right))
            i = j
        return res

# 230. Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        while curr is not None or len(stack)>0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

# 1046. Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def addone(s, val):
            l = 0
            r = len(s)-1
            while l <= r:
                mid = (l+r)//2
                if s[mid] == val:
                    return s[:mid]+[val]+s[mid:]
                elif s[mid] > val:
                    l = mid+1
                else:
                    r = mid-1
            return s[:l]+[val]+s[l:]
        
        
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0]-stones[1])
        s = sorted(stones, reverse=True)
        while len(s) > 2:
            val = s[0]-s[1]
            s.pop(0)
            s.pop(0)
            s = addone(s, val)
        return s[0]-s[1]

# 1047. Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if len(stack) == 0:
                stack.append(s)
            elif s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)

