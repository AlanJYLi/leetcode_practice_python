# 433. Minimum Genetic Mutation
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if bank == []:
            return -1
        
        seen = set()
        seen.add(start)
        level = [start]
        depth = 0
        bank = set(bank)
        while len(level) > 0:
            next_level = []
            for s in level:
                if s == end:
                    return depth
                for i in range(len(s)):
                    for j in ['A', 'C', 'G', 'T']:
                        new = s[:i]+j+s[i+1:]
                        if new not in seen and new in bank:
                            seen.add(new)
                            next_level.append(new)
            level = next_level
            depth += 1
        return -1

# 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def is_overlap(i1, i2):
            return i1[1] > i2[0]
        
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x:(x[0],x[1]))
        dp = [1] * len(intervals)
        res = 1
        for i in range(1, len(intervals)):
            temp = 0
            for j in range(i):
                if is_overlap(intervals[j], intervals[i]) == False:
                    temp = max(temp, dp[j])
            dp[i] = max(dp[i], temp+1)
            res = max(res, dp[i])
        return len(intervals)-res

