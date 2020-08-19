# 377. Combination Sum IV
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        for i in range(1, target+1):
            for v in nums:
                if v == i:
                    dp[i] += 1
                if v < i:
                    dp[i] += dp[i-v]
        return dp[-1]

# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for l in s:
            if l == ']':
                curr = stack.pop()
                temp = ''
                while curr != '[':
                    temp = curr+temp
                    curr = stack.pop()
                curr = stack.pop()
                num = ''
                while curr.isdigit() == True:
                    num = curr+num
                    if len(stack) > 0:
                        curr = stack.pop()
                    else:
                        break
                if curr.isdigit() == False:
                    stack.append(curr)
                temp = temp * int(num)
                stack.append(temp)
            else:
                stack.append(l)
        return ''.join(stack)

# 395. Longest Substring with At Least K Repeating Characters
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        store = {}
        for l in s:
            store[l] = 1 if l not in store else store[l] + 1
        
        start = 0
        res = 0
        for i, l in enumerate(s):
            if store[l] < k:
                res = max(res, self.longestSubstring(s[start:i], k))
                start = i+1
        return len(s) if start == 0 else max(res, self.longestSubstring(s[start:], k))
