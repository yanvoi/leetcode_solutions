class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {letter : i for i, letter in enumerate(alphabet)}
        to_shift = list(s)
        sum_of_shifts = 0

        for i in range(len(s) - 1, -1, -1):
            sum_of_shifts += shifts[i]
            to_shift[i] = alphabet[(mapping[s[i]] + sum_of_shifts) % 26]

        return "".join(to_shift)
