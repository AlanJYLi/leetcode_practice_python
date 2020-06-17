# 30. Substring with Concatenation of All Words
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(s) == 0:
            return []
        store = {}
        for w in words:
            store[w] = 1 if w not in store else store[w]+1
        
        l = len(words[0])
        L = len(words)*l
        res = []
        for start in range(l):
            check = {}
            substart = start
            i = start
            while i < len(s)-l+1:
                w = s[i:i+l]
                if w not in store:
                    check = {}
                    substart = i+l
                    i += l
                    continue
                if check == {} and w in store:
                    if substart + L <= len(s):
                        sub = s[substart:substart+L]
                        for j in range(0, len(sub), l):
                            temp = sub[j:j+l]
                            if temp in store:
                                check[temp] = 1 if temp not in check else check[temp]+1
                            else:
                                check = {}
                                break
                        if check == store:
                            res.append(substart)
                            substart += l
                            i += L
                        elif check == {}:
                            substart = substart+l+j
                            i = substart
                        else:
                            substart += l
                            i += L
                        continue
                    else:
                        break
                if check != {} and w in store:
                    prev = s[substart-l:substart]
                    check[w] = 1 if w not in check else check[w]+1
                    check[prev] -= 1
                    if check[prev] == 0:
                        check.pop(prev)
                    if check == store:
                        res.append(substart)
                    substart += l
                    i += l
        return res

# 31. Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums
        else:
            p = None
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    p = i
                    break
            if p is None:
                return nums.sort()
            else:
                swap = nums[p+1]
                swap_index = p+1
                for i in range(p+2, len(nums)):
                    if nums[i] <= swap and nums[i] > nums[p]:
                        swap = nums[i]
                        swap_index = i
                nums[p], nums[swap_index] = nums[swap_index],nums[p]
                l = p+1
                r = len(nums)-1
                while l<r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                return nums

# 32. Longest Valid Parentheses
class Solution: 
    # find the basic "()" and denote the corresponding position as true. 
    # Then for each group of consecutive true (e.g. f-t-t-t-t-f), check if the near 'false' position at the two sides are '(' and ')' or not. 
    # If yes, change to True and continue
    def longestValidParentheses(self, s: str) -> int:
        mask = [False] * len(s)
        for i in range(1,len(s)):
            if s[i-1] == '(' and s[i] == ')':
                mask[i-1] = True
                mask[i] = True
        
        start = 0
        end = 0
        for i in range(1, len(s)-1):
            if mask[i] == True and mask[i-1] == False:
                start = i
                continue
            if mask[i] == True and mask[i+1] == False:
                end = i
                while start > 0 and end < len(s)-1 and mask[start-1] == False and mask[end+1] == False:
                    if s[start-1] == '(' and s[end+1] == ')':
                        mask[start-1] = True
                        mask[end+1] = True
                        start -= 1
                        while start > 0 and mask[start-1] == True:
                            start -=1
                        end += 1
                        while end < len(s)-1 and mask[end+1] == True:
                            end += 1
                    else:
                        break
        count = 0
        res = 0
        for i in range(len(mask)):
            if mask[i] == True:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res,count)

class Solution:
    # dynamic programming
    # a array where ith element represents the length of the longest valid substring ending at ith index. Update the array only when ')' is meet.
    # 1. s[i] == ')' and s[i-1] == '(': array[i] = array[i-1]+2
    # 2. s[i] == ')' and s[i-1] == ')', check s[i-array[i-1]-1] == '(': array[i]=array[i-1]+2+array[i-array[i-1]-2]
    def longestValidParentheses(self, s: str) -> int:
        store = [0] * len(s)
        res = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    store[i] = store[i-2] + 2 if i>=2 else 2
                elif i-store[i-1]-1 >= 0 and s[i-store[i-1]-1] == '(':
                    store[i] = store[i-1]+store[i-store[i-1]-2]+2 if i-store[i-1]-2 >= 0 else store[i-1]+2
                res = max(res, store[i])
        return res

class Solution:
    # stack
    # initialize a stack: [-1]
    # if '(': push the index into stack
    # if ')': pop the topmost, then i-stack[-1] to get current length of valid string. Update res = max(res, i-stack[-1]). 
    # If stack[-1] doesn't exist (stack is empty), push index of this ')' into the stack because it's invalid and the new substring starts from here
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack != []:
                    res = max(res, i-stack[-1])
                else:
                    stack.append(i)
        return res

class Solution:
    # Super smart way
    # traverse from left to right, record the number of '(' (e.g. left) and ')' (e.g. right)
    # if left == right: res = max(res, 2*right); if right > left: substring sofar become invalid, reset left and right to zero
    # Then traverse from right to left, do similar thing again
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        for b in s:
            if b == '(':
                left +=1
            else:
                right += 1
            if left == right:
                res = max(res, right*2)
            elif right > left:
                left = 0
                right = 0
        left = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left +=1
            else:
                right += 1
            if left == right:
                res = max(res, left*2)
            elif left > right:
                left = 0
                right = 0
        return res