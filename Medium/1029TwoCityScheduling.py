class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        a_cost = sum(cost for cost, _ in costs)
        relocate_to_b = sorted(bcost - acost for acost, bcost in costs)

        return a_cost + sum(relocate_to_b[:len(costs) // 2])
