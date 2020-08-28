# 439. Ternary Expression Parser
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for i in range(len(expression)):
            stack.append(expression[i])
            if i < len(expression)-1 and expression[i+1] != ':':
                continue
            while len(stack) > 1 and stack[-2] == ':':
                latter = stack.pop()
                temp1 = stack.pop()
                former = stack.pop()
                temp2 = stack.pop()
                stack.append(former if stack.pop() == 'T' else latter)
        return stack.pop()

class Solution: # recursion, faster than using stack
    def parseTernary(self, expression: str) -> str:
        if expression in ('T', 'F') or expression.isdigit() == True:
            return expression
        
        question_count = 1
        flag = expression[0] == 'T'
        for i in range(2, len(expression)):
            c = expression[i]
            if c == '?':
                question_count += 1
            elif c == ':':
                question_count -= 1
            if question_count == 0:
                remain = expression[2:i] if flag == True else expression[i+1:]
                return self.parseTernary(remain)

# 442. Find All Duplicates in an Array (do it without extra space and in O(n) runtime)
class Solution: 
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[int(abs(nums[i])-1)] *= (-1.0)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0 and type(nums[i]) != int:
                res.append(i+1)
        return res

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n)-1] *= (-1)
        res = []
        for n in nums:
            if nums[abs(n)-1] > 0:
                res.append(abs(n))
                nums[abs(n)-1] *= (-1)
        return res