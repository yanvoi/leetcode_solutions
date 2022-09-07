class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert the new interval the same way as in insertion sort
        intervals.append(newInterval)
        i = len(intervals) - 2
        
        while i >= 0 and newInterval[0] < intervals[i][0]:
            intervals[i+1] = intervals[i]
            i -= 1
        intervals[i+1] = newInterval
        
        # merge all intervals
        merged = []
        for interval in intervals:
            
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
    
