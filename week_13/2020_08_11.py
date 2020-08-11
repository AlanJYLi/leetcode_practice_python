# 307. Range Sum Query - Mutable
class NumArray:

    def __init__(self, nums: List[int]):
        if nums != []:
            self.nums = nums
            self.cumsum = [0] * len(nums)
            self.cumsum[0] = nums[0]
            for i in range(1, len(nums)):
                self.cumsum[i] = nums[i] + self.cumsum[i-1]

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i, len(self.nums)):
            self.cumsum[j] += diff

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.cumsum[j]
        else:
            return self.cumsum[j] - self.cumsum[i-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

# 311. Sparse Matrix Multiplication
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                for j in range(len(B[0])):
                    res[i][j] += A[i][k]*B[k][j]
        return res

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0: # take advantage of sparse matrix
                    for j in range(len(B[0])):
                        res[i][j] += A[i][k]*B[k][j]
        return res

# 313. Super Ugly Number
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        idx = [0] * len(primes)
        nums = [1] * len(primes)
        res = [1]
        curmin = 1
        for i in range(1, n):
            for j in range(len(primes)):
                if nums[j] == curmin:
                    nums[j] = res[idx[j]] * primes[j]
                    idx[j] += 1
            curmin = min(nums)
            res.append(curmin)
        return res[-1]

# 314. Binary Tree Vertical Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        store = {}
        if root is None:
            return []
        
        queue = [(root,0)] # tree, column
        while len(queue) > 0:
            num_tree = len(queue)
            for _ in range(num_tree):
                curr_tree, column = queue.pop(0)
                if column not in store:
                    store[column] = [curr_tree.val]
                else:
                    store[column].append(curr_tree.val)
                if curr_tree.left is not None:
                    queue.append((curr_tree.left, column-1))
                if curr_tree.right is not None:
                    queue.append((curr_tree.right, column+1))
        res = []
        min_col = min(store.keys())
        max_col = max(store.keys())
        for i in range(min_col, max_col+1):
            res.append(store[i])
        return res

# 318. Maximum Product of Word Lengths
class Solution: # exceed time limit
    def maxProduct(self, words: List[str]) -> int:
        def string_bit(s):
            record = ['0'] * 26
            for ch in set(s):
                record[25-ord(ch)+ord('a')] = '1'
            return int(''.join(record), 2)
        
        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                w1 = words[i]
                w2 = words[j]
                if string_bit(w1) & string_bit(w2) == 0:
                    res = max(res, len(w1)*len(w2))
        return res

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def string_bit(s):
            record = ['0'] * 26
            for ch in set(s):
                record[25-ord(ch)+ord('a')] = '1'
            return int(''.join(record), 2)
        
        word_num = [] # store the numerica representation of strings
        length = []
        for w in words:
            word_num.append(string_bit(w))
            length.append(len(w))
        
        res = 0
        for i in range(len(word_num)-1):
            for j in range(i+1, len(word_num)):
                if word_num[i] & word_num[j] == 0:
                    res = max(res, length[i]*length[j])
        return res