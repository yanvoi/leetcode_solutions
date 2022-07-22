class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        current_altitude = 0
        max_altitude = 0
        
        for num in gain:
            current_altitude += num
            if max_altitude < current_altitude:
                max_altitude = current_altitude
                
        return max_altitude
    
