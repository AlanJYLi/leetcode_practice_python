# 1150. Check If a Number Is Majority Element in a Sorted Array
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[l] == target and nums[r] == target:
                break
            elif nums[l] != target and nums[r] == target:
                l += 1
            elif nums[l] == target and nums[r] != target:
                r -= 1
            else:
                l += 1
                r -= 1
        return r-l+1 > len(nums)/2

# 1160. Find Words That Can Be Formed by Characters
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        store = {}
        for s in chars:
            store[s] = store[s]+1 if s in store else 1
        
        res = 0
        for w in words:
            if len(w) > len(chars):
                continue
            else:
                w_store = {}
                flag = 0
                for s in w:
                    if s not in store:
                        flag = 1
                        continue
                    else:
                        w_store[s] = w_store[s]+1 if s in w_store else 1
                if flag == 0:
                    flag2 = 0
                    for s in w_store:
                        if w_store[s] > store[s]:
                            flag2 = 1
                            continue
                    if flag2 == 0:
                        res += len(w)
        return res

# 1165. Single-Row Keyboard
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        store = {keyboard[0]:0}
        i = 1
        prev = 0
        res = 0
        for s in word:
            while s not in store:
                store[keyboard[i]] = i
                i += 1
            res += abs(store[s]-prev)
            prev = store[s]
        return res

# 1180. Count Substrings with Only One Distinct Letter
class Solution:
    def countLetters(self, S: str) -> int:
        res = 0
        i = 0
        while i < len(S):
            j = i+1
            while j < len(S):
                if S[j] == S[i]:
                    j += 1
                else:
                    break
            l = j-i
            res += ((l+1)*l)//2
            i = j
        return res

# 1184. Distance Between Bus Stops
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        subsum = sum(distance[start:destination]) if start<=destination else sum(distance[destination:start])
        return min(subsum, total-subsum)
