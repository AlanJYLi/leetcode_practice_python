# 276. Paint Fence
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0 :
            return 0
        
        # painting the first post with a certain color
        # n:[a,b,c]
        # a:total number of choice at the nth post
        # b:between the (n-1)th post and nth post, how many ways they are painted with same color
        # c:between the (n-1)th post and nth post, how many ways they are painted with different color
        # for the (n+1)th post, the number of options are determined by b, c at nth post
        store = {1:[1,0,0], 2:[k,1,k-1]}
        for i in range(3,n+1):
            adjacent = store[i-1][1]
            not_adjacent = store[i-1][2]
            total = adjacent*(k-1) + not_adjacent*k
            store[i] = [total, not_adjacent, total-not_adjacent]
        
        # we can start with k different colors
        return store[n][0]*k

# 278. First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1) == True:
            return 1
        if isBadVersion(n-1) == False:
            return n
        
        l = 1
        r = n
        
        while r - l > 1:
            mid = (l+r) // 2
            if isBadVersion(mid) == False:
                l = mid
            else:
                r = mid
        return r

# 283. Move Zeroes
class Solution: # two pointer
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        
        letter_word = {}
        word_letter = {}
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            if letter not in letter_word:
                if word not in word_letter:
                    letter_word[letter] = word
                    word_letter[word] = letter
                else:
                    return False
            else:
                if letter_word[letter] != word:
                    return False
                else:
                    continue
        return True

# 292. Nim Game
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0

# 293. Flip Game
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        
        if len(s) <= 1:
            return res
        
        for i in range(0,len(s)-1):
            if s[i:i+2] == '++':
                ns = s[:i] + '--' + s[i+2:]
                res.append(ns)
        
        return res

# 299. Bulls and Cows
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        s_dic = {}
        g_dic = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s_dic[secret[i]] = 1 if secret[i] not in s_dic else s_dic[secret[i]]+1
                g_dic[guess[i]] = 1 if guess[i] not in g_dic else g_dic[guess[i]]+1
        
        for num in s_dic:
            if num in g_dic:
                cow += min(s_dic[num], g_dic[num])
        
        return str(bull)+'A'+str(cow)+'B'

# 303. Range Sum Query - Immutable
class NumArray:

    def __init__(self, nums: List[int]):
        self.sumdict = {-1:0}
        for i in range(len(nums)):
            self.sumdict[i] = self.sumdict[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sumdict[j] - self.sumdict[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 326. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n % 3 == 0:
            n = n // 3
        
        return n == 1

# 339. Nested List Weight Sum
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def dfs(nestedList, depth):
            total = 0
            if nestedList.isInteger() == True:
                total += nestedList.getInteger() * depth
            else:
                for n in nestedList.getList():
                    total += dfs(n, depth+1)
            return total
        
        total = 0
        depth = 1
        for n in nestedList:
            total += dfs(n, depth)
        return total

# 342. Power of Four
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        
        if num < 1:
            return False
        
        list_binary = bin(num).split('1')
        return len(list_binary) == 2 and len(list_binary[-1])%2 == 0 

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        import math
        return num>0 and math.log2(num) % 2 == 0

# 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0 or len(s) == 1:
            return s
        
        l = 0
        r = len(s)-1
        
        while r-l >= 0:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# 345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a':0, 'e':0, 'i':0, 'o':0 ,'u':0}
        position = []
        for i in range(len(s)):
            if s[i].lower() in vowel:
                position.append(i)
        
        sl = list(s)
        
        l = 0
        r = len(position)-1
        while r>l:
            sl[position[l]], sl[position[r]] = sl[position[r]], sl[position[l]]
            l += 1
            r -= 1
        return ''.join(sl)