# 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {0: cost[0], 1: cost[1]}
        cost = cost + [0]
        for i in range(2,len(cost)):
            c = cost[i]
            store[i] = min(store[i-2]+c, store[i-1]+c)
        return store[len(cost)-1]

# 747. Largest Number At Least Twice of Others
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            if nums[0]>=nums[1]:
                max1, max2, index = nums[0], nums[1], 0
            else:
                max1, max2, index = nums[1], nums[0], 1
            i = 2
            while i < len(nums):
                if nums[i] > max1:
                    max2 = max1
                    max1 = nums[i]
                    index = i
                elif max1 >= nums[i] > max2:
                    max2 = nums[i]
                i += 1
            return index if max1>=2*max2 else -1

# 748. Shortest Completing Word
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        store = {}
        total = 0
        for l in licensePlate:
            if l.isalpha():
                total += 1
                l = l.lower()
                if l in store:
                    store[l] += 1
                else:
                    store[l] = 1
        res = ''
        minlength = float(inf)
        for w in words:
            if len(w) < total or len(w) > minlength:
                continue
            else:
                if all(w.count(l) >= store[l] for l in store):
                    if len(w) < minlength:
                        res = w
                        minlength = len(w)
        return res

# 758. Bold Words in String
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        if words == [] or S == '':
            return S
        else:
            n = len(S)
            bold = [False]*n
            for i in range(n):
                sub = S[i:]
                for w in words:
                    if sub.startswith(w):
                        for j in range(i, min(i+len(w),n)):
                            bold[j] = True
            res = ''
            for i in range(n):
                if bold[i] == True and (i == 0 or bold[i-1] == False):
                    res = res + '<b>'
                res = res + S[i]
                if bold[i] == True and (i == n-1 or bold[i+1] == False):
                    res = res + '</b>'
            return res

# 760. Find Anagram Mappings
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        store = {}
        for i in range(len(B)):
            if B[i] not in store:
                store[B[i]] = [i]
            else:
                store[B[i]].append(i)
        res = []
        for num in A:
            res.append(store[num].pop(0))
        return res

# 762. Prime Number of Set Bits in Binary Representation
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        
        def isPrime(n):
            if n == 1:
                return False
            else:
                root = int(sqrt(n))
                while root > 1:
                    if n % root == 0:
                        return False
                    root -= 1
                return True
        
        prime = {}
        count = 0
        for n in range(L, R+1):
            b = bin(n)
            bits = b.count('1')
            if bits in prime:
                if prime[bits]:
                    count += 1
            else:
                prime[bits] = isPrime(bits)
                if prime[bits]:
                    count += 1
        return count

# 766. Toeplitz Matrix
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        if M == 1 or N == 1:
            return True
        else:
            for i in range(1, M):
                row1 = matrix[i-1]
                row2 = matrix[i]
                if row1[:-1] != row2[1:]:
                    return False
            return True

# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(l) for l in J])

# 783. Minimum Distance Between BST Nodes
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res = res + inorder(root.right)
            return res
        
        res = inorder(root)
        best = res[1] - res[0]
        for i in range(2, len(res)):
            best = min(best, res[i]-res[i-1])
        return best

# 784. Letter Case Permutation
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [[]]
        for l in S:
            n = len(res)
            if l.isalpha():
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(l.lower())
                    res[n+i].append(l.upper())
            else:
                for i in range(n):
                    res[i].append(l)
        
        return map(''.join, res)

# 788. Rotated Digits
class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for n in range(1, N+1):
            s = str(n)
            if '3' not in s and '4' not in s and '7' not in s and ('2' in s or '5' in s or '6' in s or '9' in s):
                count += 1
        return count

# 796. Rotate String
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif A == B:
            return True
        else:
            for i in range(1,len(A)):
                sub = A[i:]
                if B.startswith(sub):
                    if A[:i] == B[-i:]:
                        return True
            return False

# 800. Similar RGB Color
class Solution:
    def similarRGB(self, color: str) -> str:
        res = '#'
        for i in range(1, len(color), 2):
            sub = color[i:i+2]
            if sub[0] == sub[1]:
                res += sub
            else:
                num = int(sub, 16)
                n = num // 17
                res = res + '{:02x}'.format(17*n) if abs(num-n*17) <= abs(num-(n+1)*17) else res + '{:02x}'.format(17*(n+1))
        return res