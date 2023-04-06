# recursive
# class Solution:
#     def coloredCells(self, n: int) -> int:

#         if n == 1:
#             return 1

#         return (n - 1) * 4 + self.coloredCells(n - 1)

class Solution:
    def coloredCells(self, n: int) -> int:

        return 1 + sum(4 * i for i in range(n))
