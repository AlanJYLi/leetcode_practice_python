# 143. Reorder List
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        
        store = None
        temp = None
        while second_half is not None:
            temp = second_half.next
            second_half.next = store
            store = second_half
            second_half = temp
        reverse = store
       
        c1 = head
        c2 = reverse
        while c2 is not None:
            temp = c1.next
            c1.next = c2
            temp2 =c2.next
            c2.next = temp
            c1 = temp
            c2 = temp2

# 144. Binary Tree Preorder Traversal
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root):
            res = []
            if root:
                res.append(root.val)
                res = res + preorder(root.left)
                res = res + preorder(root.right)
            return res
        
        return preorder(root)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res

# 145. Binary Tree Postorder Traversal
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root):
            res = []
            if root:
                res = postorder(root.left)
                res = res+postorder(root.right)
                res.append(root.val)
            return res
        
        return postorder(root)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return res[::-1]

# 146. LRU Cache
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.store = dict()
        self.used = [] #used as a stack

    def get(self, key: int) -> int:
        if key in self.store:
            self.used.remove(key)
            self.used.append(key)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self.used.remove(key)
            self.used.append(key)
        else:
            if self.c != len(self.store):
                self.store[key] = value
                self.used.append(key)
            else:
                remove_key = self.used.pop(0)
                self.store.pop(remove_key)
                self.store[key] = value
                self.used.append(key)
# if solving in O(1) time complexity, use OrderedDict (from collections import OrderedDict)

# 147. Insertion Sort List
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode: 
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0, head)
        curr = dummy.next
        val = curr.next.val
        last = curr
        remain = curr.next.next
        curr.next = None
        while remain is not None:
            if val >= last.val:
                last.next = ListNode(val)
                last = last.next
                val = remain.val
                remain = remain.next
                curr = dummy.next
            elif val < curr.val:
                dummy.next = ListNode(val, curr)
                val = remain.val
                remain = remain.next
                curr = dummy.next
            else:
                while curr.next is not None:
                    if val < curr.next.val:
                        curr.next = ListNode(val, curr.next)
                        val = remain.val
                        remain = remain.next
                        curr = dummy.next
                        break
                    curr = curr.next
        
        if val >= last.val:
            last.next = ListNode(val)
        elif val < curr.val:
            dummy.next = ListNode(val, curr)
        else:
            while curr.next is not None:
                if val < curr.next.val:
                    curr.next = ListNode(val, curr.next)
                    break
                curr = curr.next
        return dummy.next

# 148. Sort List
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def mergeTwo(h1, h2):
            dummy = ListNode(0)
            curr = dummy
            while h1 is not None and h2 is not None:
                if h1.val <= h2.val:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next
            curr.next = h1 if h1 is not None else h2
            return dummy.next
        
        
        def divideSort(h):
            if h is None or h.next is None:
                return h
            
            slow = h
            fast = h.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            
            second_half = slow.next
            slow.next = None
            first_half = h
            first_sort = divideSort(first_half)
            second_sort = divideSort(second_half)
            return mergeTwo(first_sort, second_sort)
        
        return divideSort(head)

# 149. Max Points on a Line
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def slope(a,b):
            dx = a[0]-b[0]
            dy = a[1]-b[1]
            if dy == 0:
                return (0,0)
            elif dx == 0:
                return (-1,-1) 
                # use a pair of invalid numbers to represent
                # we ensure dx and dy not to be negative at the same time
            elif dx < 0:
                dx = -dx
                dy = -dy
            import math
            a = math.gcd(dx,dy)
            return (dx/a, dy/a)
            
        count = {}
        unique = set()
        for p in points:
            pt = tuple(p)
            count[pt] = 1 if pt not in count else count[pt]+1
            unique.add(pt)
        unique = list(unique)
        
        if len(unique) == 1:
            return count[tuple(unique[0])]
        
        res = 0
        for i in range(len(unique)):
            temp = {}
            for j in range(len(unique)):
                if i != j:
                    s = slope(unique[i], unique[j])
                    if s not in temp:
                        temp[s] = count[unique[i]]+ count[unique[j]]
                    else:
                        temp[s] += count[unique[j]]
            for s in temp:
                res = max(res, temp[s])
        return res

# 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s.isdigit():
                stack.append(s)
            elif len(s) > 1:
                stack.append(s)
            else:
                a2 = stack.pop()
                a1 = stack.pop()
                if s == '+':
                    a = int(a1)+int(a2)
                    stack.append(str(a))
                elif s == '-':
                    a = int(a1)-int(a2)
                    stack.append(str(a))
                elif s == '*':
                    a = int(a1)*int(a2)
                    stack.append(str(a))
                else:
                    if int(a1) / int(a2) >= 0:
                        a = int(a1)//int(a2)
                    else:
                        a = -(abs(int(a1))//abs(int(a2)))
                    stack.append(str(a))
        return int(stack[0])


