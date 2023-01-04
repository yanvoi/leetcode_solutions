class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        count = dict()
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        rounds = 0
        for num in count.values():
            if num == 1:
                return -1
            if num % 3 == 0:
                rounds += num // 3
            else:
                rounds += (num // 3) + 1

        return rounds
