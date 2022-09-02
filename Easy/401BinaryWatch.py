class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        ans = []
        
        for hour in range(12):
            for minute in range(60):
                if minute < 10:
                    time = f'{hour}:0{minute}'
                else:
                    time = f'{hour}:{minute}'
                        
                if (bin(hour) + bin(minute)).count('1') == turnedOn: ans.append(time)
                    
        return ans
        
