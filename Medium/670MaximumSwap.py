# First attempt - O(n^2) - Nonoptimal
class Solution:
    def maximumSwap(self, num: int) -> int:

        number = [int(n) for n in str(num)]

        for starting_index in range(len(number)):
            swap_index = starting_index

            for i in range(starting_index + 1, len(number)):
                if number[i] >= number[swap_index]:
                    swap_index = i

            if number[swap_index] > number[starting_index]:
                number[starting_index], number[swap_index] = number[swap_index], number[starting_index]
                break

        return int(''.join([str(n) for n in number]))
