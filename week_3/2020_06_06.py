# 599. Minimum Index Sum of Two Lists
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        store = {}
        for i in range(len(list1)):
            store[list1[i]] = i
        
        store_sum = {}
        for i in range(len(list2)):
            if list2[i] in store:
                store_sum[list2[i]] = i + store[list2[i]]
        
        best = min(store_sum.values())
        res = []
        for r in store_sum:
            if store_sum[r] == best:
                res.append(r)
        return res

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        store = {}
        for i in range(len(list1)):
            store[list1[i]] = i
        
        minsum = len(list1)+len(list2)
        res = []
        j = 0
        while j < len(list2) and j <= minsum:
            if list2[j] in store:
                if j + store[list2[j]] < minsum:
                    res = [list2[j]]
                    minsum = j + store[list2[j]]
                elif j + store[list2[j]] == minsum:
                    res.append(list2[j])
            j += 1
        return res

# 604. Design Compressed String Iterator
class StringIterator:

    def __init__(self, compressedString: str):
        import re
        self.letter = re.split('[0-9]+', compressedString)[:-1]
        self.num = [int(x) for x in re.split('[a-zA-Z]+', compressedString)[1:]]
        self.curr_letter = 0
        self.curr_num = 0
        self.total = 0

    def next(self) -> str:
        if self.letter == []:
            return ' '
        if self.total > sum(self.num):
            self.total += 1
            return ' '
        elif self.total == sum(self.num[:self.curr_num+1]):
            self.curr_letter += 1
            self.curr_num += 1
            self.total += 1
            return self.letter[self.curr_letter] if self.curr_letter < len(self.letter) else ' '
        else:
            self.total += 1
            return self.letter[self.curr_letter]
        
    def hasNext(self) -> bool:
        if self.total < sum(self.num):
            return True
        else:
            return False
        
# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# 605. Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
        
        start = flowerbed[0]
        end = 0
        total = 0
        count_zero = 0
        for i in range(len(flowerbed)):
            end = flowerbed[i]
            if flowerbed[i] == 0:
                count_zero += 1
            else:
                if count_zero-start-end > 0:
                    plant = (count_zero-start-end+1)//2
                else:
                    plant = 0
                total += plant
                if total >= n:
                    return True
                start = end
                count_zero = 0
        if count_zero > 0:
            if count_zero-start-end > 0:
                plant = (count_zero-start-end+1)//2
            else:
                plant = 0
            total += plant
            return total >= n
        return total >= n

class Solution: # clean one: scan along the list
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        total = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                total += 1
                flowerbed[i] = 1
            if total >= n:
                return True
        return False