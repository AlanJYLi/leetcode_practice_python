# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if nums[i] not in element:
                element[remain] = i
            else:
                index = element[nums[i]]
                return [index, i]

# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        upper = 2**31-1
        lower = -2**31
        while x != 0:
            if x >= 0:
                pop = x % 10
            else:
                if x % 10 == 0:
                    pop = 0
                else:
                    pop = x % 10 - 10
            x = (x-pop) // 10
            
            if (rev > upper/10) or (rev == upper//10 and pop > 7):
                return 0      
            if (rev < lower/10) or (rev == (lower-(lower%10-10))//10 and pop < -8):
                return 0         
            rev = rev*10+pop
            
        return rev

# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = 0
            initial = x
            while x != 0:
                pop = x % 10
                x = x // 10
                rev = rev*10+pop
            if initial == rev:
                return True

class Solution: # only need to compare the first half and the second half
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x>=0 and x<10:
            return True
        elif x % 10 == 0:
            return False
        else:
            rev = 0
            while rev < x:
                pop = x % 10
                x = x // 10
                rev = 10*rev + pop
            return (rev == x) or (rev // 10 == x)

# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        lettermap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000, 
                     'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        length = len(s)
        n = 0
        i = 0
        while i < length:
            if i+2 <= length:
                letters = s[i:i+2]
                if letters in lettermap:
                    n = n+lettermap[letters]
                    i = i+2
                    continue
            letter = s[i]
            n = n+lettermap[letter]
            i=i+1
        return n

# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            scanword = strs[0]
            for i in range(len(scanword)):
                letter = scanword[i]
                for word in strs[1:]:
                    if i >= len(word) or letter != word[i]:
                        return pre
                pre = pre+letter
            return pre

# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        front = ['(','{','[']
        end= [')','}',']']
        if len(s) == 0:
            return True
        elif len(s)%2 != 0:
            return False
        elif s[0] in end:
            return False
        else:
            front = ['(','{','[']
            end= [')','}',']']
            stack = [s[0]]
            for p in s[1:]:
                if p in front:
                    stack.append(p)
                if p in end:
                    if p==')' and stack[-1] != '(':
                        return False
                    elif p=='}' and stack[-1] != '{':
                        return False
                    elif p==']' and stack[-1] != '[':
                        return False
                    else:
                        stack = stack[:-1]
            return len(stack) == 0