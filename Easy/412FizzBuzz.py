class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["".join(val for key, val in ((3, "Fizz"), (5, "Buzz")) if not i % key) or str(i) for i in range(1, n + 1)]
