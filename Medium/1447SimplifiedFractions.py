class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        answer = []
        for numerator in range(1, n):
            for denominator in range(numerator + 1, n + 1):
                # Greatest Common Divisor must be equal to 1
                # only then will a fraction be simplified
                if gcd(numerator, denominator) == 1:
                    answer.append(str(numerator) + '/' + str(denominator))

        return answer
