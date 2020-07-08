# 1030. Matrix Cells in Distance Order
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        store = {}
        maxd = 0
        for i in range(R):
            for j in range(C):
                d = abs(r0-i)+abs(c0-j)
                maxd = max(maxd, d)
                if d in store:
                    store[d].append([i,j])
                else:
                    store[d] = [[i,j]]
        res = []
        for i in range(maxd+1):
            res = res+store[i]
        return res

# 1033. Moving Stones Until Consecutive
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        s = sorted([a,b,c])
        a,b,c = s[0], s[1], s[2]
        maxres = c-b-1+b-a-1
        if maxres == 0:
            return [0,0]
        
        if b-a <= 2 or c-b <= 2:
            return [1, maxres]
        else:
            return [2, maxres]

# 1037. Valid Boomerang
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a0,b0 = points[0][0],points[0][1]
        a1,b1 = points[1][0],points[1][1]
        a2,b2 = points[2][0],points[2][1]
        
        if (a0,b0)==(a1,b1) or (a0,b0)==(a2,b2) or (a1,b1)==(a2,b2):
            return False
        if (a0==a1 and a1==a2) or (b0==b1 and b1==b2):
            return False
        if (a1-a0)*(b2-b1) == (b1-b0)*(a2-a1):
            return False
        return True

# 222. Count Complete Tree Nodes
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def process(root):
            if root is None:
                return 0
            return 1+process(root.left)+process(root.right)
        
        return process(root)

# 223. Rectangle Area
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        S1 = abs(A-C)*abs(B-D)
        S2 = abs(G-E)*abs(H-F)
        
        if C < E:
            return S1+S2
        if A > G:
            return S1+S2
        if B > H:
            return S1+S2
        if D < F:
            return S1+S2
        if S1 == 0 or S2 == 0:
            return S1+S2
        return -min(abs(G-A),abs(C-E),abs(A-C),abs(G-E))*min(abs(H-B),abs(D-F),abs(B-D),abs(H-F))+S1+S2
