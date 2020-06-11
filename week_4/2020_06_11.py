# 804. Unique Morse Code Words
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store = set()
        for w in words:
            c = ''
            for l in w:
                c = c + code[ord(l)-ord('a')]
            store.add(c)
        return len(store)

# 806. Number of Lines To Write String
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        res = [1, 0]
        total_w = 0
        for l in S:
            w = widths[ord(l)-ord('a')]
            if w + total_w <= 100:
                total_w += w
            else:
                res[0] += 1
                total_w = w
        res[1] = total_w
        return res

# 811. Subdomain Visit Count
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = {}
        for s in cpdomains:
            r = s.split()
            if r[1] not in store:
                store[r[1]] = int(r[0])
            else:
                store[r[1]] += int(r[0])
            domain = r[1].split('.')
            if domain[-1] not in store:
                store[domain[-1]] = int(r[0])
            else:
                store[domain[-1]] += int(r[0])
            if len(domain) == 3:
                address = domain[1]+'.'+domain[2]
                if address not in store:
                    store[address] = int(r[0])
                else:
                    store[address] += int(r[0])
        res = []
        for key in store:
            s = str(store[key])+' '+key
            res.append(s)
        return res

class Solution: # cleaner code
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = {}
        for s in cpdomains:
            r = s.split()
            count = int(r[0])
            add = r[1].split('.')
            for i in range(len(add)):
                domain = '.'.join(add[i:])
                store[domain] = count if domain not in store else store[domain]+count
        res = []
        for key in store:
            s = str(store[key])+' '+key
            res.append(s)
        return res

# 812. Largest Triangle Area
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(three_point):
            a = three_point[0]
            b = three_point[1]
            c = three_point[2]
            return 0.5*abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-b[0]*a[1]-c[0]*b[1]-a[0]*c[1])
        
        import itertools
        best = 0
        for three_point in itertools.combinations(points,3):
            best = max(best, area(three_point))
        return best

# 819. Most Common Word
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c,' ')
        words = paragraph.split()
        store = {}
        for w in words:
            w = w.lower()
            store[w] = 1 if w not in store else store[w]+1
        
        banned = set(banned)
        best = 0
        res = ''
        for w in store:
            if w not in banned and store[w]>best:
                best = store[w]
                res = w
        return res

# 821. Shortest Distance to a Character
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = [0] * len(S)
        p = []
        for i in range(len(S)):
            if S[i] == C:
                p.append(i)
        for i in range(len(p)):
            if i == 0:
                for j in range(p[i]):
                    res[j] = p[i] - j
            else:
                for j in range(p[i-1]+1, p[i]):
                    res[j] = min(j-p[i-1], p[i]-j)
        for j in range(p[-1]+1, len(S)):
            res[j] = j - p[-1]
        return res

# 824. Goat Latin
class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = S.split()
        store = []
        for i in range(len(s)):
            new = ''
            if s[i][0].lower() in {'a','e','i','o','u'}:
                new = s[i] + 'ma'
            else:
                new = s[i][1:] + s[i][0] + 'ma'
            new = new + 'a'*(i+1)
            store.append(new)
        return ' '.join(store)

# 830. Positions of Large Groups
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        if len(S) <= 2:
            return res
        else:
            curr = 0
            count = 1
            for j in range(1,len(S)):
                if S[j] == S[curr]:
                    count += 1
                else:
                    if count >= 3:
                        res.append([curr, j-1])
                    curr = j
                    count = 1
            if count >= 3:
                res.append([curr,j])
            return res

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    res.append([i,j])
                i = j+1
        return res

# 832. Flipping an Image
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def process(row):
            row = [1-x for x in row[::-1]]
            return row
        
        for i in range(len(A)):
            A[i] = process(A[i])
        return A

# 836. Rectangle Overlap
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1]) 

# 840. Magic Squares In Grid
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(a,b,c,d,e,f,g,h,i):
            if e != 5:
                return False
            else:
                return (sorted([a,b,c,d,e,f,g,h,i]) == [1,2,3,4,5,6,7,8,9] and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))
        
        count = 0
        for l in range(len(grid)-2):
            for w in range(len(grid[0])-2):
                if isMagic(grid[l][w],grid[l][w+1],grid[l][w+2],grid[l+1][w],grid[l+1][w+1],grid[l+1][w+2],grid[l+2][w],grid[l+2][w+1],grid[l+2][w+2]):
                    count += 1
        return count

# 844. Backspace String Compare
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(s):
            stack = []
            for l in s:
                if l != '#':
                    stack.append(l)
                elif l == '#' and len(stack)> 0:
                    stack.pop()
            return stack
        
        return process(S) == process(T)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        import re
        def process(a):
            while re.search('[a-z]{1}#{1}', a) != None:
                a = re.sub('[a-z]{1}#{1}', '', a)
            return a
        return process(S).replace('#','') == process(T).replace('#','')

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def resultgenerator(a):
            skip = 0
            for x in a[::-1]:
                if x == '#':
                    skip += 1
                elif x != '#' and skip > 0:
                    skip -= 1
                else:
                    yield x
        
        s = [x for x in resultgenerator(S)]
        t = [x for x in resultgenerator(T)]
        return s == t

# 849. Maximize Distance to Closest Person
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        p = []
        for i in range(len(seats)):
            if seats[i] == 1:
                p.append(i)
        if p[0] == 0:
            best = 1
        else:
            best = p[0]
        for i in range(1,len(p)):
            d = (p[i]-p[i-1]) // 2
            best = max(best, d)
        if p[-1] != len(seats)-1:
            best = max(best, len(seats)-1-p[-1])
        return best

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        best = 0
        leftedge = 0 # seats starts from 1
        count = 0
        for i in range(len(seats)):
            if i == 0 and seats[i] == 0:
                count += 1
                leftedge = 1 # seats starts from 0
            elif i == len(seats)-1 and seats[i] == 0:
                count += 1
                best = max(best, count)
            elif seats[i] == 0:
                count += 1
            else:
                if leftedge == 1:
                    best = max(best, count)
                    leftedge = 0
                    count = 0
                else:
                    best = max(best, (count+1)//2)
                    count = 0
        return best

# 852. Peak Index in a Mountain Array
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A)-1
        while r>l:
            mid = (r+l) // 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]:
                l = mid + 1
            elif A[mid-1] > A[mid] > A[mid+1]:
                r = mid -1
        return r

# 859. Buddy Strings
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif A == B:
            return len(set(A)) < len(A)
        else:
            position = 0
            count = 0
            for i in range(len(A)):
                if A[i] != B[i] and count == 0:
                    count += 1
                    position = i
                elif A[i] != B[i] and count == 1:
                    count += 1
                    if A[i] != B[position] or B[i] != A[position]:
                        return False
                elif A[i] != B[i] and count == 2:
                    return False
            return count == 2

# 860. Lemonade Change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if five == 0:
                    return False
                elif 0 < five < 3 and ten == 0:
                    return False
                else:
                    if ten > 0:
                        ten -= 1
                        five -= 1
                    else:
                        five -= 3
        return True

# 867. Transpose Matrix
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        l = len(A)
        w = len(A[0])
        B = []
        for i in range(w):
            B.append([0]*l)
        for i in range(l):
            for j in range(w):
                B[j][i] = A[i][j]
        return B

# 868. Binary Gap
class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N).split('b')[-1]
        best = 0
        curr = 0
        for i in range(1,len(s)):
            if s[i] == '1':
                best = max(best, i-curr)
                curr = i
        return best

# 872. Leaf-Similar Trees
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def process(root):
            res = []
            if root:
                if root.left is None and root.right is None:
                    res.append(root.val)
                res = res + process(root.left)
                res = res + process(root.right)
            return res

        return process(root1) == process(root2)

# 874. Walking Robot Simulation
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        best = 0
        p = [0,0]
        d = 1 #direction: 1-north, 2-east, 3-south, west-4 
        ob = set([(x,y) for [x,y] in obstacles])
        for num in commands:
            if num == -2:
                d = d-1 if d>1 else 4
            elif num == -1:
                d = d+1 if d<4 else 1
            else:
                for i in range(1,num+1):
                    p[d%2] = p[d%2] + (-2*(d//3)+1)*1
                    if (p[0], p[1]) in ob:
                        p[d%2] = p[d%2] - (-2*(d//3)+1)*1
                        break
                best = max(best, (p[0]**2+p[1]**2))
        return best