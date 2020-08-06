# 1497. Check If Array Pairs Are Divisible by k
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        store = {}
        for num in arr:
            store[num%k] = 1 if num%k not in store else store[num%k]+1
       
        for i in range(k//2+1):
            if i == 0 or i*2 == k:
                if i not in store:
                    continue
                else:
                    if store[i] % 2 != 0:
                        return False
            else:
                if i not in store:
                    if k-i in store:
                        return False
                else:
                    if k-i not in store or store[i] != store[k-i]:
                        return False
        return True

# 1498. Number of Subsequences That Satisfy the Given Sum Condition
class Solution: # exceed time limit
    def numSubseq(self, nums: List[int], target: int) -> int:
        def count_sub(sub, l, r):
            if l >= r:
                return 0
            if (l,r) in self.seen:
                return count_sub(sub[1:], l+1, r)+count_sub(sub[:-1], l, r-1)
            else:
                self.seen.add((l,r))
                if len(sub) == 1:
                    return 1 if sub[0]*2 <= target else 0
                else:
                    if sub[0]+sub[-1] <= target:
                        return 2**(len(sub)-2)+count_sub(sub[1:], l+1, r)+count_sub(sub[:-1], l, r-1)
                    else:
                        return count_sub(sub[1:], l+1, r)+count_sub(sub[:-1], l, r-1)
        
        nums.sort()
        self.seen = set()
        res = count_sub(nums, 0, len(nums))
        return res

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if 2*nums[i] <= target:
                res += 1
            
            l, r = i+1, len(nums)-1
            while l < r:
                mid = (l+r)//2+1
                if nums[i] + nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid
            
            if nums[i] + nums[r] <= target:
                res += 2**(r-i)-1
            
        return res % (10**9 + 7)

# 1502. Can Make Arithmetic Progression From Sequence
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or max(arr) == min(arr):
            return True
        
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True


