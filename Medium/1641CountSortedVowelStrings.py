class Solution:
    def countVowelStrings(self, n: int) -> int:

        # combination with repetitions
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // math.factorial(4)
