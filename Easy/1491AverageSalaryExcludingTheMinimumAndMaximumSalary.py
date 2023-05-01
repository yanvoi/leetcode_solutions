class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

# single pass version
# class Solution:
#     def average(self, salary: List[int]) -> float:
#         max_salary, min_salary, total_sum = -inf, inf, 0
#         for s in salary:
#             max_salary, min_salary = max(max_salary, s), min(min_salary, s)
#             total_sum += s

#         return (total_sum - max_salary - min_salary) / (len(salary) - 2)
