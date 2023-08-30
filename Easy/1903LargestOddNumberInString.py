class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_index = len(num) - 1
        while last_index >= 0 and int(num[last_index]) % 2 == 0: last_index -= 1
        return num[:last_index + 1]
