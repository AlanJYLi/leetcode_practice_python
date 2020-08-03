# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

# 1471. The k Strongest Values in an Array
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if k == len(arr):
            return arr    
        arr.sort()
        m = arr[(len(arr)-1)//2]
        res = []
        l = 0
        r = len(arr)-1
        while l < r:
            if abs(arr[r]-m) >= abs(arr[l]-m):
                res.append(arr[r])
                r -= 1
            else:
                res.append(arr[l])
                l += 1
            if len(res) == k:
                return res

# 1474. Delete N Nodes After M Nodes of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        temp = head
        while temp is not None:
            i = 0
            while temp is not None and i < m-1:
                temp = temp.next
                i += 1
            if temp is None:
                break
            prev = temp
            temp = temp.next
            i = 0
            while temp is not None and i < n:
                temp = temp.next
                i += 1
            prev.next = temp
        return head

# 1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = [0] * len(prices)
        for i in range(len(prices)):
            if i == 0:
                stack.append(((prices[i]),i))
            else:
                val = prices[i]
                while len(stack) > 0:
                    if val > stack[-1][0]:
                        stack.append((val, i))
                        break
                    else:
                        p, idx = stack.pop()
                        res[idx] = p - val
                stack.append((val, i))
        while len(stack) > 0:
            p, idx = stack.pop()
            res[idx] = p
        return res

# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start_from = 0
        window_sum = 0
        res = float(inf)
        dp = [float(inf)] * len(arr)
        for idx, num in enumerate(arr):
            window_sum += num
            while window_sum > target:
                window_sum -= arr[start_from]
                start_from += 1
            if window_sum == target:
                curr_length = idx - start_from + 1
                res = min(res, curr_length+dp[start_from-1])
                dp[idx] = min(curr_length, dp[idx-1])
            else:
                dp[idx] = dp[idx-1]
        return res if res < float(inf) else -1
