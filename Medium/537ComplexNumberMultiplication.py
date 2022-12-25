class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        real1, imaginary1 = num1.split('+')
        real2, imaginary2 = num2.split('+')

        real = (int(real1) * int(real2)) + (int(imaginary1[:-1]) * int(imaginary2[:-1]) * -1)
        imaginary = (int(real1) * int(imaginary2[:-1])) + (int(real2) * int(imaginary1[:-1]))

        return str(real) + '+' + str(imaginary) + 'i'
