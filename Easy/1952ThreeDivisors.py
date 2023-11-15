# I could check if n is a multiple of 2 primes but I don't have
# enough time to implement it
class Solution:
    def isThree(self, n: int) -> bool:
        return sum(not n % num for num in range(1, n + 1)) == 3
