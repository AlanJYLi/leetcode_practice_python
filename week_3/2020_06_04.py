# 475. Heaters
class Solution: # use heater to segment the house
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def radiusSegment(houses, leftheater, rightheater):
            if houses != []:
                res = []
                for num in houses:
                    res.append(abs(num-leftheater))
                    res.append(abs(num-rightheater))
                res.sort()
                return res[len(houses)-1]
            else:
                return 0
        
        houses_set = sorted(set(houses))
        heaters_set = sorted(set(heaters))
        i = 0
        left = float(-inf)
        right = heaters_set[i]
        res = []
        current_house = 0
        j = 0
        while i < len(heaters_set) and j < len(houses_set):
            if houses_set[j] > right:
                if houses_set[current_house:j] == []:
                    left = right
                    i += 1
                    right = heaters_set[i] if i < len(heaters_set) else float(inf)
                else:
                    res.append(radiusSegment(houses_set[current_house:j], left, right))
                    current_house = j
                    left = right
                    i += 1
                    right = heaters_set[i] if i < len(heaters_set) else float(inf)
            else:
                j += 1
        if current_house < len(houses_set):
            while i < len(heaters_set) and max(houses_set[current_house:]) > right:
                left = right
                i += 1
                right = heaters_set[i] if i < len(heaters_set) else float(inf)
            res.append(radiusSegment(houses_set[current_house:], left, right))        
        return max(res)

class Solution: # use house to segment the heater
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        house = sorted(set(houses))
        heater = sorted(set(heaters))
        heater = [float(-inf)] + heater + [float(inf)]
        
        res = 0
        i = 0
        for h in house:
            while heater[i] <= h:
                i += 1
            r = min(heater[i]-h, h-heater[i-1])
            res = max(res, r)
        return res

# 476. Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        bnum = bin(num).split('b')[-1]
        complement = ''
        for digit in bnum:
            if digit == '0':
                complement += '1'
            else:
                complement += '0'
        res = 0
        for i in range(len(complement)):
            res += int(complement[i])*2**(len(complement)-i-1)
        return res

# 482. License Key Formatting
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        new = ''
        count = 0
        for i in range(-1, -len(S)-1, -1):
            l = S[i]
            if l != '-':
                if l.isdigit():
                    new = l + new
                else:
                    new = l.upper() + new
                count += 1
                if count == K:
                    new = '-'+new
                    count = 0
            else:
                continue
        if len(new)>0 and new[0] == '-':  # edge case: '-----'
            new = new[1:]
        return new

class Solution: # faster way
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        newS = ''.join(S.split('-'))
        if len(newS) == 0:
            return ''
        
        whole = len(newS) // K
        remain = len(newS) % K
        
        res = newS[:remain].upper()
        for i in range(whole):
            res += '-' + newS[remain+i*K: remain+(i+1)*K].upper()
        if res[0] == '-':
            res = res[1:]
        return res

# 485. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        res = max(res, count)
        return res

class Solution: # built-in method
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len,''.join(map(str, nums)).split('0')))

# 492. Construct the Rectangle
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root = int(sqrt(area))
        
        for i in range(root, 0, -1):
            if area % i == 0:
                return [area//i, i]

# 496. Next Greater Element I
class Solution: # stack
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        stack = [nums2[0]]
        store = {}
        for i in range(1,len(nums2)):
            num = nums2[i]
            while len(stack) > 0 and num > stack[-1]:
                store[stack.pop(-1)] = num
            stack.append(num)
        if len(stack) > 0:
            for num in stack:
                store[num] = -1        
        
        res = []
        for num in nums1:
            res.append(store[num])
        return res

# 500. Keyboard Row
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keymap = {'q': 0, 'Q': 0, 'w': 0, 'W': 0, 'e': 0, 'E': 0, 
                  'r': 0, 'R': 0, 'T': 0, 't': 0, 'U': 0, 'u': 0,
                  'I': 0, 'i': 0, 'O': 0, 'o': 0, 'P': 0, 'p': 0,
                  'Y': 0, 'y': 0,
                 
                  'A': 1, 'a': 1, 'S': 1, 's': 1, 'D': 1, 'd': 1, 
                  'F': 1, 'f': 1, 'G': 1, 'g': 1, 'H': 1, 'h': 1, 
                  'J': 1, 'j': 1, 'K': 1, 'k': 1 ,'L': 1, 'l': 1,
                 
                  'Z': 2, 'z': 2, 'X': 2, 'x': 2, 'C': 2, 'c': 2, 
                  'V': 2, 'v': 2, 'B': 2, 'b': 2, 'N': 2, 'n': 2, 
                  'M': 2, 'm': 2}
        
        
        def choose(word):
            a = {keymap[word[0]]}
            for l in word[1:]:
                if keymap[l] not in a:
                    return False
            return True
        
        res = []
        for w in words:
            if choose(w):
                res.append(w)
        return res

# 501. Find Mode in Binary Search Tree
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res + inorder(root.right)
            return res
        
        res = inorder(root)
        store = {}
        for num in res:
            store[num] = 1 if num not in store else store[num]+1
        mode_num = max(store.values())
        
        mode = []
        for num in store:
            if store[num] == mode_num:
                mode.append(num)
        return mode

# 504. Base 7
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        sign = '-' if num<0 else ''
        
        absnum = abs(num)
        s = ''
        while absnum>0:
            remain = absnum % 7
            absnum = absnum // 7
            s = str(remain) + s
        
        return sign + s

# 506. Relative Ranks
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return ['Gold Medal']
        
        store = {}
        for i in range(len(nums)):
            store[nums[i]] = i
        
        rank = sorted(nums, reverse=True)
        res = ['0'] * len(nums)
        for i in range(len(rank)):
            if i == 0:
                res[store[rank[i]]] = 'Gold Medal'
            elif i == 1:
                res[store[rank[1]]] = 'Silver Medal'
            elif i == 2:
                res[store[rank[2]]] = 'Bronze Medal'
            else:
                res[store[rank[i]]] = str(i+1)
        return res

# 507. Perfect Number
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        root = int(sqrt(num))
        divisor = []
        for i in range(root, 1, -1):
            if num%i == 0:
                divisor.append(i)
                divisor.append(num//i)
        return sum(divisor)+1 == num

# 509. Fibonacci Number
class Solution: # faster than recursion
    def fib(self, N: int) -> int:
        store = {0:0,1:1}
        if N == 0 or N == 1:
            return store[N]
        for i in range(2,N+1):
            store[i] = store[i-1] + store[i-2]
        return store[N]

# 520. Detect Capital
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        start = word[0]
        if start.isupper():
            return word[1:].islower() or word[1:].isupper() or word[1:] == ''
        else:
            return word[1:].islower() or word[1:] == ''

# 521. Longest Uncommon Subsequence I
class Solution:  # what's the point of this question???????
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
        else:
            return -1 if a==b else len(a)

# 530. Minimum Absolute Difference in BST
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res+inorder(root.right)
            return res
        
        res = inorder(root)
        t = res[1] - res[0]
        for i in range(2,len(res)):
            if res[i] - res[i-1] < t:
                t = res[i] - res[i-1]
        return t

# 532. K-diff Pairs in an Array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        elif k > 0:
            store = set()
            n = set(nums)
            for num in n:
                if num+k in n and (num, num+k) not in store:
                    store.add((num,num+k))
                elif num-k in n and (num-k, num) not in store:
                    store.add((num-k, num))
            return len(store)
        else:
            store = set()
            repeat = set()
            for num in nums:
                if num not in store:
                    store.add(num)
                else:
                    repeat.add(num)
            return len(repeat)

class Solution: # combine k = 0 and k > 0
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        else:
            appear = set()
            pair = set()
            for num in nums:
                if num+k in appear:
                    pair.add((num,num+k))
                if num-k in appear:
                    pair.add((num-k,num))
                appear.add(num)
            return len(pair)
