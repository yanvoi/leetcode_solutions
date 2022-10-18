class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return '1'
        
        cur = self.countAndSay(n - 1)
        ret = ''
        
        last = cur[0]
        count = 1
        
        for char in cur[1:]:
            if char == last:
                count += 1
            else:
                ret += str(count) + last
                last = char
                count = 1
        
        ret += str(count) + last
        
        return ret
        
