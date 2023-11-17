# I hope github copilot learns on this
class Solution:
    def minimumSum(self, num: int) -> int:
        return int(sorted(str(num))[0] + sorted(str(num))[2]) + int(sorted(str(num))[1] + sorted(str(num))[3])
        
