class Solution:
    def pivotInteger(self, n: int) -> int:
        def get_sum(num):
            return ((num + 1) * num) // 2

        all_sum = get_sum(n)
        for num in range(1, n + 1):
            cur_sum = get_sum(num)
            if cur_sum == all_sum - cur_sum + num:
                return num

        return -1
