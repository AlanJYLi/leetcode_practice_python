# 110. Balanced Binary Tree
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self. maxDepth(root.right)
            return 1+max(left,right)
    
    def compareDepth(self, root):
        if root is None:
            return True
        else:
            if abs(self.maxDepth(root.left)-self.maxDepth(root.right))<=1:
                return True
            else:
                return False
            
    
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        while root is not None:
            if self.compareDepth(root)==False:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(root):
            if root is None:
                return 0         
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        
        if root is None:
            return True
        if abs(maxDepth(root.left) - maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

# 111. Minimum Depth of Binary Tree
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        tree = []
        tree.append(root)
        count = 1
        
        while len(tree) > 0:
            num_trees = len(tree)
            for i in range(num_trees):
                temp_tree = tree.pop(0)         
                if temp_tree.left is None and temp_tree.right is None:
                    return count
                else:
                    if temp_tree.left is not None:
                        tree.append(temp_tree.left)
                    if temp_tree.right is not None:
                        tree.append(temp_tree.right)
            count += 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1

# 112. Path Sum
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return sum == root.val
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        if numRows == 0:
            return pascal
        if numRows == 1:
            pascal.append([1])
            return pascal
        elif numRows == 2:
            pascal.append([1])
            pascal.append([1,1])
            return pascal
        else:
            pascal = [[1],[1,1]]
            while numRows > 2:
                new = [1]
                temp =pascal[-1]
                for i in range(len(temp)-1):
                    new.append(temp[i]+temp[i+1])
                new.append(1)
                pascal.append(new)
                numRows -= 1
            return pascal

# 119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = []
        if rowIndex == 0:
            pascal.append([1])
            return pascal[-1]
        elif rowIndex == 1:
            pascal.append([1])
            pascal.append([1,1])
            return pascal[-1]
        else:
            pascal = [[1],[1,1]]
            while rowIndex > 1:
                new = [1]
                temp =pascal[-1]
                for i in range(len(temp)-1):
                    new.append(temp[i]+temp[i+1])
                new.append(1)
                pascal.append(new)
                rowIndex -= 1
            return pascal[-1]

# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1]-prices[0])
        else:
            profit = max(0, prices[1]-prices[0])
            for i in range(2, len(prices)):
                profit = max(profit, prices[i]-min(prices[:i]))
            return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        curr_min = prices[0]
        curr_max = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            val = prices[i]
            if val > curr_max:
                curr_max = val
                profit = max(profit, curr_max-curr_min)
            if val < curr_min:
                curr_min = val
                curr_max = val
        return profit

# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        curr_min = prices[0]
        curr_max = prices[0]
        curr_profit = 0
        total = 0
        
        for i in range(1,len(prices)):
            val = prices[i]
            if val > curr_max:
                curr_max = val
                curr_profit = curr_max - curr_min
                total += curr_profit
                curr_min = val
            else:
                curr_profit = curr_max - curr_min
                curr_max = val
                curr_min = val
                total += curr_profit
        return total

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        else:
            valley = prices[0]
            peak = prices[0]
            i = 0
            total = 0
            while i < len(prices)-1:
                while i < len(prices)-1 and prices[i] >= prices[i+1]:
                    i += 1
                valley = prices[i]
                while i < len(prices)-1 and prices[i] <= prices[i+1]:
                    i += 1
                peak = prices[i]
                total = total + peak - valley
            return total

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''
        for l in s:
            if l.isalnum():
                s_clean += l.lower()
        
        return s_clean == s_clean[::-1]

# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = {}
        for n in nums:
            if n not in store:
                store[n] = 1
            else:
                store.pop(n)
        return list(store.keys())[0]

# 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        store = {}
        while head is not None:
            if head in store:
                return True
            else:
                store[head] = 0
            
            head = head.next

class Solution: # two pointer with different speed
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next
        
        while True:
            if fast is None or fast.next is None:
                return False
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                return True

# 155. Min Stack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append((x,x))
        else:
            current_min = self.data[-1][1]
            self.data.append((x, min(x, current_min)))

    def pop(self) -> None:
        self.data.pop(-1)

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 157. Read N Characters Given Read4
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n == 0:
            return n
        else:
            times = n // 4
            remain = n % 4
            i = 0
            while times > 0:
                buf4 = ['','','','']
                l = read4(buf4)
                buf[i:i+l] = buf4
                i = i+l
                times = times-1
            if remain > 0:
                buf4 = ['','','','']
                l = read4(buf4)
                l = min(remain,l)
                buf[i:i+l] = buf4[:l]
                i = i+l
            return i

# 160. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        else:
            store = {}
            while headA is not None:
                store[headA] = 0
                headA = headA.next
            while headB is not None:
                if headB in store:
                    return headB             
                headB = headB.next
            
            return None

class Solution: # a tricky way from leetcode solution, but slower than the approach above
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        pa = headA
        pb = headB
        
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
            
        return pa

# 167. Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i = i+1
            else:
                j = j-1
        return [i+1, j+1]

# 168. Excel Sheet Column Title
class Solution:
    def convertToTitle(self, n: int) -> str:
        A_int = ord('A')
        result = ''
        while n != 0:
            remain = (n-1) % 26
            n = (n-1) // 26
            result = chr(A_int+remain) + result
        return result

# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        threshold = len(nums) // 2 + 1
        store = {}
        for n in nums:
            if n not in store:
                store[n] = 1
            else:
                store[n] += 1
                if store[n] == threshold:
                    return n

# another smart way: sort the array, and the majority element must be the element in the middle

# 170. Two Sum III - Data structure design
class TwoSum: # slower than the second approach

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        store = {}
        for i in range(len(self.data)):
            remain = value - self.data[i]
            if remain not in store:
                store[self.data[i]] = i
            else:
                return True
        return False

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.data:
            self.data[number] = 1
        else:
            self.data[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.data.keys():
            remain = value - num
            if num != remain:
                if remain in self.data:
                    return True
            else:
                if self.data[num] > 1:
                    return True
        
        return False
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

