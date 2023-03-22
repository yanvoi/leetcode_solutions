class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # looking from the right - find the first digit that's smaller than it's predeccessor
        digits = list(str(n))
        i = len(digits) - 1
        while i - 1 >= 0 and digits[i - 1] >= digits[i]:
            i -= 1

        # if the digits are sorted in non-descending order
        # you can't make a bigger number out of given digits
        if i == 0:
            return -1

        # looking from the left of the found digit
        # find the first that is greater than that digit
        j = i
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1

        # swap those 2 digits
        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        # reverse the second half of the digits so they are now in non-ascending order
        digits[i:] = reversed(digits[i:])

        answer = int("".join(map(str, digits)))
        return answer if answer < (1 << 31) else -1
