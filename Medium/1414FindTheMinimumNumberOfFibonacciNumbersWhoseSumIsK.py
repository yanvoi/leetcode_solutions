class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 2]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        answer, index = 0, len(fib) - 1
        while k:
            if fib[index] > k:
                index -= 1
                continue
            k -= fib[index]
            answer += 1

        return answer
