# 436. Find Right Interval
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            return [-1]
        
        for i in range(len(intervals)):
            intervals[i].append(i)
        
        sort_start = sorted(intervals, key=lambda x:x[0])
        sort_end = sorted(intervals, key=lambda x:x[1])
        res = [-1] * len(intervals)
        j = 0
        for i in range(len(sort_end)):
            temp = sort_end[i]
            while j < len(sort_start):
                scan = sort_start[j]
                if temp[1] > scan[0]:
                    j += 1
                else:
                    break
            if j == len(sort_start):
                break
            res[temp[2]] = scan[2]
        return res

# 438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        p_code = [0]*26
        s_code = [0]*26
        
        for l in p:
            p_code[ord(l)-ord('a')] +=1
        
        res = []
        for i in range(len(s)):
            s_code[ord(s[i])-ord('a')] += 1
            if i >= len(p):
                s_code[ord(s[i-len(p)])-ord('a')] -= 1
            if s_code == p_code:
                res.append(i-len(p)+1)
        return res

