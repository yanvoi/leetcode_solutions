class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        self.str1, self.str2 = str1, str2
        for i in range(min(len(str1), len(str2)), 0, -1):
            if self.is_common_divisor(i):
                return str1[:i]

        return ''
        

    def is_common_divisor(self, i):

        if len(self.str1) % i or len(self.str1) % i:
            return False

        base = self.str1[:i]
        multiply1, multiply2 = len(self.str1) // i, len(self.str2) // i

        return self.str1 == base * multiply1 and self.str2 == base * multiply2
