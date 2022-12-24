# This solution is far from being optimal but it's the most intuitive one
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.s = s
        self.answer = []
        self.__dfs__(0, [])
        return self.answer


    def __dfs__(self, index, cur_s):
        if index == len(self.s):
            self.answer.append(cur_s)
            return

        for i in range(index+1, len(self.s) + 1):
            next_bit = self.s[index:i]
            if self.__is_palindrome__(next_bit):
                self.__dfs__(i, cur_s + [next_bit])


    def __is_palindrome__(self, s):
        return s == s[::-1]
        
