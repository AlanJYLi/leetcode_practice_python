# 418. Sentence Screen Fitting
class Solution: # exceed time limit
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        idx = 0
        n = len(sentence)
        i = 1
        j = 0
        while i <= rows:
            w = sentence[idx%n]
            if j+len(w) <= cols:
                j = j+len(w)+1
            else:
                j = len(w)+1
                i += 1
            idx += 1
        return (idx-1)//n

class Solution: # cache the number of sentence in a row when the row is started with each word
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        for w in sentence:
            if len(w) > cols:
                return 0
        
        store = {}
        res = 0
        idx = 0
        r = 1
        n = len(sentence)
        while r <= rows:
            pos = 0
            start = idx
            if start not in store:
                count = 0
                while pos < cols:
                    if pos+len(sentence[idx]) > cols:
                        break
                    else:
                        pos = pos+len(sentence[idx])+1
                        idx += 1
                        idx = idx%n
                        if idx == 0:
                            count += 1
                            res += 1
                        store[start] = [idx, count] # store the start word for next row and number of sentence completed in this row
            else:
                idx, number = store[start]
                res += number
            r += 1
        return res

# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        res = 0
        most = 0
        start = 0
        end = 0
        while end < len(s):
            store[s[end]] = 1 if s[end] not in store else store[s[end]]+1
            most = max(most, store[s[end]])
            if end-start+1-most > k:
                store[s[start]] -= 1
                start += 1
            else:
                res = max(res, end-start+1)
            end += 1
        return res

# 426. Convert Binary Search Tree to Sorted Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left is None and root.right is None:
            root.left = root
            root.right = root
            return root
        
        def in_order(root):
            res = []
            if root:
                res = in_order(root.left)
                res.append(root)
                res = res + in_order(root.right)
            return res
        
        res = in_order(root)
        for i in range(len(res)):
            if i == 0:
                res[i].left = res[-1]
                res[i].right = res[i+1]
            elif i == len(res)-1:
                res[i].left = res[i-1]
                res[i].right = res[0]
            else:
                res[i].left = res[i-1]
                res[i].right = res[i+1]
        return res[0]

