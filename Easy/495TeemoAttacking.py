class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        time = 0
        
        if len(timeSeries) > 0:
            time += duration
        
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i-1] < duration:
                time += timeSeries[i] - timeSeries[i-1]
            else:
                time += duration
                
        return time
