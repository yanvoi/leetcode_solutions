# to understand this solution we need to make some observation
# we can make an n-bit gray code by taking an (n-1)-bit gray code
# and concatenating it with 1 + reversed((n-1)-bit gray code)   <== (in a bit sense)

# then all the adjacent integers will differ by 1 bit
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 0: return [0]

        shorter_code = self.grayCode(n - 1)
        return shorter_code + [(1<<(n - 1)) + num for num in shorter_code[::-1]]
