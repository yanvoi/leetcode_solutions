class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        stack, nums = [], set()
        for char in word:
            if char.isdigit():
                stack.append(char)
            elif stack:
                nums.add(int("".join(stack)))
                stack = []

        nums.add(int("".join(stack))) if stack else None
        return len(nums)
