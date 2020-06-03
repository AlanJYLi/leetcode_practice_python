# 408. Valid Word Abbreviation
class Solution: # split the abbr into letters and numbers
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        
        abbr_split = []
        num = 0
        j = 0
        while j < len(abbr):
            a = abbr[j]
            if a.isdigit():
                if a == '0' and num == 0: # edge cases: 'a0b', 'a02b'
                    return False
                num = num*10 + int(a)
                j = j + 1
            else:
                if num > 0:
                    abbr_split.append(num)
                abbr_split.append(a)
                num = 0
                j = j + 1
        if num > 0:
            abbr_split.append(num)
        
        i = 0
        j = 0
        while i<len(word) and j<len(abbr_split):
            if type(abbr_split[j]) == int:
                if abbr_split[j] == 0:
                    return False
                else:
                    i = i + abbr_split[j]
                    j = j + 1
            else:
                if word[i] != abbr_split[j]:
                    return False
                else:
                    i = i + 1
                    j = j + 1
        return i == len(word) and j == len(abbr_split)

class Solution: # similar approach with two pointers
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        
        i = 0
        j = 0
        while i<len(word) and j<len(abbr):
            if abbr[j].isdigit() == False:
                if abbr[j] != word[i]:
                    return False
                else:
                    j += 1
                    i += 1
            else:
                if abbr[j] == '0':
                    return False
                else:
                    num = 0
                    while j<len(abbr) and abbr[j].isdigit():
                        num = num*10+int(abbr[j])
                        j += 1
                    i = i+num
        return i == len(word) and j == len(abbr)     

# 409. Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        store = {}
        for l in s:
            if l in store:
                store[l] += 1
            else:
                store[l] = 1
        
        total = 0
        have_odd_count = 0
        for l in store:
            num = store[l]
            if num % 2 == 0:
                total += num
            else:
                have_odd_count = 1
                total += (num-1)
        return total + have_odd_count

# 412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res

# 414. Third Maximum Number
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return float(-inf)
        
        maxnum = set()
        for num in nums:
            maxnum.add(num)
            if len(maxnum) > 3:
                maxnum.remove(min(maxnum))
        return min(maxnum) if len(maxnum) == 3 else max(maxnum)

# 415. Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = '0' + num1 # deal with 1+9 or 99+2
        n2 = '0' + num2
        if len(n1) < len(n2):
            n1, n2 = n2, n1      
        n2 = '0'*(len(n1)-len(n2))+n2  
        
        res = ''
        tenth = 0
        for i in range(-1, -len(n1)-1, -1):
            d1 = n1[i]
            d2 = n2[i]
            add = int(d1) + int(d2) + tenth
            if add < 10:
                res = str(add) + res
                tenth = 0
            else:
                res = str(add%10) + res
                tenth = 1
        
        for i in range(len(res)):
            if res[i] != '0':
                return res[i:]
        return '0'

# 422. Valid Word Square
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        max_word_length = 0
        for i in range(n):
            w = words[i]
            max_word_length = max(max_word_length, len(w))
            for j in range(n):
                if i == j:
                    continue
                else:
                    w1 = words[i]
                    l1 = w1[j] if j<len(w1) else ''
                    w2 = words[j]
                    l2 = w2[i] if i<len(w2) else ''
                    if l1 != l2:
                        return False
        return max_word_length == n

# 434. Number of Segments in a String
# 'ad  df  '.split() = ['ad','df']
# 'ad  df  '.split(' ') = ['ad','','df','','']
class Solution:
    def countSegments(self, s: str) -> int:
        res = s.strip().split(' ') 
        count = 0
        for seg in res:
            if seg != '':
                count += 1
        return count

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

# 437. Path Sum III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def sumWithRoot(root, total=0): # For a certain tree, get the all possible sum from the root
            if root is not None:
                total += root.val
                store[total] = 1 if total not in store else store[total]+1
                if root.left is None and root.right is None:
                    pass
                else:
                    sumWithRoot(root.left, total)
                    sumWithRoot(root.right, total)
        
        while root is None:
            return 0
        
        stack = [root]
        count = 0
        while len(stack) > 0:
            curr = stack.pop()
            store = {sum:0}
            sumWithRoot(curr, 0)
            count += store[sum]
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return count

class Solution: # a better way
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count = [0]
        target = sum
        
        def getSum(root, store):
            if root is None:
                return 
            
            store = [x+root.val for x in store]
            store.append(root.val)
            count[0] += store.count(target)
            getSum(root.left, store)
            getSum(root.right, store)
        
        getSum(root, [])
        return count[0]

# 441. Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n 
        l = 1
        r = n
        while l<=r:
            mid = (l+r)//2
            sum1 = (1+mid)*mid//2
            sum2 = (1+mid+1)*(mid+1)//2
            if sum1<=n and sum2>n:
                return mid
            elif sum1>n:
                r = mid - 1
            elif sum2==n:
                return mid+1
            else:
                l = mid + 1

# 443. String Compression
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1 or chars == []:
            return len(chars)
        
        curr = chars[0]
        write = 1
        count = 1
        for i in range(1,len(chars)):
            letter = chars[i]
            if letter != curr and count == 1:
                chars[write] = letter
                curr = letter
                write += 1
            elif letter != curr and count > 1:
                for digit in str(count):
                    chars[write] =digit
                    write += 1
                chars[write] = letter
                write += 1
                curr = letter
                count = 1
            elif letter == curr:
                count += 1
        if count > 1:
            for digit in str(count):
                chars[write] =digit
                write += 1
        return write

# 447. Number of Boomerangs
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p,q):
            return (p[0]-q[0])**2+(p[1]-q[1])**2
        
        def count(store):
            total = 0
            for d in store:
                if store[d] > 1:
                    total += store[d] * (store[d]-1)
            return total
        
        store = {}
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                d = distance(points[i], points[j])
                if i not in store:
                    store[i] = {d:1}
                else:
                    if d not in store[i]:
                        store[i][d] = 1
                    else:
                        store[i][d] += 1
                if j not in store:
                    store[j] = {d:1}
                else:
                    if d not in store[j]:
                        store[j][d] = 1
                    else:
                        store[j][d] += 1
        
        total = 0
        for k in store:
            total += count(store[k])
        
        return total

# 448. Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        store = {}
        for i in range(1, len(nums)+1):
            store[i] = 1
        
        for num in nums:
            if num in store:
                store.pop(num)
        
        return list(store.keys())

class Solution: # solution without extra space: regard each val as index of the list and turn the value to negative if the position is visited
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

# 453. Minimum Moves to Equal Array Elements
class Solution: # increasing n-1 elements equals to decreasing 1 element. So total number of moves equals to decreasing each element to min(list) one by one 
    def minMoves(self, nums: List[int]) -> int:
        total = 0
        minnum = min(nums)
        for num in nums:
            if num != minnum:
                total += num-minnum
        return total

# 455. Assign Cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == []:
            return 0
        
        g_sort = sorted(g)
        s_sort = sorted(s)
        
        i = 0
        j = 0
        while i<len(g_sort) and j<len(s_sort):
            if g_sort[i] <= s_sort[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i

# 459. Repeated Substring Pattern
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        start = s[0]
        for i in range(1,len(s)):
            if s[i] == start:
                sub = s[:i]
                if len(s) % len(sub) == 0 and sub*(len(s)//len(sub)) == s:
                    return True
        return False

# 461. Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

# 463. Island Perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # the land cell connected with n water cells: n
        length = len(grid)
        width = len(grid[0])
        
        total = 0
        for i in range(length):
            for j in range(width):
                land = grid[i][j]
                if land == 1:
                    count = 0
                    left = j-1
                    right = j+1
                    upper = i-1
                    below = i+1
                    count += int(left<0 or grid[i][left]==0)
                    count += int(right>width-1 or grid[i][right]==0)
                    count += int(upper<0 or grid[upper][j]==0)
                    count += int(below>length-1 or grid[below][j]==0)
                    total += count
        return total
