# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        wl = s.strip().split()
        return ' '.join(wl[::-1])

# 152. Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        
        res = nums[0]
        dp = [[0,0] for i in range(len(nums))]
        dp[0][0] = res
        dp[0][1] = res
        for i in range(1,len(nums)):
            val = nums[i]
            dp[i][0] = max(val, val*dp[i-1][0], val*dp[i-1][1])
            dp[i][1] = min(val, val*dp[i-1][0], val*dp[i-1][1])
            res = max(res, dp[i][0])
        return res

# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            left = nums[mid-1]
            right = nums[mid+1]
            val = nums[mid]
            if val < right and val < left:
                return val
            elif val > left and val > right:
                return right
            elif val > nums[l] and val < right:
                l = mid+1
            elif val < nums[r] and val > left:
                r = mid-1

# 154. Find Minimum in Rotated Sorted Array II
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l] > nums[l+1]:
                return nums[l+1]
            elif nums[r-1] > nums[r]:
                return nums[r]
            elif nums[l] >= nums[r]:
                l += 1
                r -= 1
        return nums[r]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            val = nums[mid]
            if nums[r] < nums[l] <= nums[mid]:
                l = mid+1
            elif nums[mid] <= nums[r] < nums[l]:
                r = mid
            elif nums[l] < nums[r]:
                break
            else:
                l += 1
        return nums[l]

# 156. Binary Tree Upside Down
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None or root.left is None:
            return root
        
        stack = [root]
        new = TreeNode(root.val)
        while len(stack) > 0:
            curr = stack.pop()
            if curr.left is not None:
                stack.append(curr.left)
                new = TreeNode(curr.left.val, curr.right, new)
        return new

class Solution: # leetcode: swap
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        prev = None
        prev_right = None
        while root:
            root.right, root.left, prev_right, prev, root = prev, prev_right, root.right, root, root.left
        return prev

# 159. Longest Substring with At Most Two Distinct Characters
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == '':
            return 0
        
        store = {}
        res = 0
        i = 0
        j = 0
        while i < len(s):
            while j < len(s):
                while len(store) <= 2 and j < len(s):
                    l = s[j]
                    if l not in store:
                        store[l] = 1
                    else:
                        store[l] += 1
                    j += 1
                res = max(res, j-1-i)
                if j == len(s):
                    if len(store) <= 2:
                        res = max(res, j-i)
                    break
                while i < j-2:
                    l = s[i]
                    if store[l] == 1:
                        store.pop(l)
                    else:
                        store[l] -= 1
                    i += 1
                    if len(store) <= 2:
                        break
            if j == len(s):
                break
        return res

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        
        res = 2
        start = 0
        end = 0
        store = {}
        while end < len(s):
            if len(store) < 3:
                store[s[end]] = end
                end += 1
            if len(store) == 3:
                leftmost = min(store.values())
                store.pop(s[leftmost])
                start = leftmost+1
            
            res = max(res, end-start)
        return res

# 161. One Edit Distance
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t)) > 1:
            return False
        
        if s == t:
            return False
        
        if len(s) > len(t):
            s, t = t, s
        
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                return s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        return True

# 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l 

# 163. Missing Ranges
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            return [str(lower)+'->'+str(upper)] if lower < upper else [str(lower)]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                val = nums[i]
                if lower == val:
                    pass
                elif lower == val-1:
                    res.append(str(lower))
                else:
                    res.append(str(lower)+'->'+str(val-1))
            if i >= 0 and i<len(nums)-1:
                l = nums[i]
                r = nums[i+1]
                if l >= r-1:
                    pass
                elif l == r-2:
                    res.append(str(l+1))
                else:
                    res.append(str(l+1)+'->'+str(r-1))
            if i == len(nums)-1:
                val = nums[i]
                if upper == val:
                    pass
                elif upper == val+1:
                    res.append(str(upper))
                else:
                    res.append(str(val+1)+'->'+str(upper))
        return res

class Solution: # clear way
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        
        res = []
        for i in range(len(nums)-1):
            l = nums[i]
            r = nums[i+1]
            if l <= r-2:
                s = str(l+1)+'->'+str(r-1) if l+1<r-1 else str(l+1)
                res.append(s)
        return res

# 164. Maximum Gap
class Solution: # to achieve linear time complexity, use radix sort (nearly linear time complexity)
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0]-nums[1])
        
        num_remains = [0] * len(nums)
        check = [nums[i]-num_remains[i] for i in range(len(nums))]
        i = 0
        store = [[] for k in range(10)]
        while sum(check)>0:
            store = [[] for k in range(10)]
            remain = [[] for k in range(10)]
            t = 10**i
            for j in range(len(nums)):
                val = nums[j]
                r = num_remains[j]
                digit = (val-r)//t%10
                store[digit].append(val)
                remain[digit].append(digit*t+r)
            nums = []
            for bucket in store:
                nums += bucket
            num_remains = []
            for bucket in remain:
                num_remains += bucket
            check = [nums[i]-num_remains[i] for i in range(len(nums))]
            i += 1
        
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i]-nums[i-1])
        return res

# 165. Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        sign = 1
        if len(v1) > len(v2):
            v1, v2 = v2, v1
            sign = -1
        
        for i in range(len(v1)):
            a = v1[i]
            b = v2[i]
            if int(a) < int(b):
                return -1*sign
            elif int(a) > int(b):
                return 1*sign
            else:
                continue
        if i == len(v2)-1:
            return 0
        else:
            for j in range(i+1, len(v2)):
                if int(v2[j]) == 0:
                    continue
                else:
                    return -1*sign
            return 0

# 166. Fraction to Recurring Decimal
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        def getrepeat(a,b):
            remain = -1
            n = a
            s = ''
            seen = {a:0}
            i = 1
            while remain not in seen:
                if remain == -1:
                    seen[remain] = -1
                else:
                    seen[remain] = i
                    i += 1
                while n < b:
                    n = n*10
                    if n < b:
                        s += '0'
                        if n not in seen:
                            seen[n] = i
                            i += 1
                if n%b == 0:
                    s = s+str(n//b)
                    return s, False, seen[-1]
                else:
                    s = s+str(n//b)
                    remain = n%b
                    n = remain
            return s, True, seen[remain]
        
        if numerator == 0:
            return '0'
        if numerator*denominator<0:
            s = '-'
        else:
            s = ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        if numerator%denominator == 0:
            return s+str(numerator//denominator)
        else:
            s = s+str(numerator//denominator) + '.'
            temp, check, position = getrepeat(numerator%denominator,denominator)
            if check == False:
                return s+temp
            else:
                s = s+temp[:position]
                s = s+'('+temp[position:]+')'
                return s
