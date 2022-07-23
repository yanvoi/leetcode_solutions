class Solution:
    def digitCount(self, num: str) -> bool:
        
        h = dict()
        
        for i in range(len(num)):
            h[i] = num[i]
            
        for i in h:
            if num.count(str(i)) != int(h[i]):
                return False
            
        return True
        
