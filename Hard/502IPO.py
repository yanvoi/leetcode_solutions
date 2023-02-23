# NOTE TO SELF: PROFIT == INCOME - CAPITAL where INCOME >= CAPITAL
# MEANING WE CAN ONLY HAVE MORE MONEY IN NEXT ITERATIONS

# greedy algorithm - we keep all the projects we can afford in each iteration
# and at the end of an iteration we finish the one that brings us the most profit
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        heap = []
        projects = sorted(zip(profits, capital), key=lambda x: x[1])

        cur_added_project = 0
        for _ in range(k):
            # add all the new (more and more expensive) projects we can currently afford to the queue
            while cur_added_project < len(projects) and projects[cur_added_project][1] <= w:
                # this is a min heap so we push the negative value of the profit onto it
                heapq.heappush(heap, -projects[cur_added_project][0])
                cur_added_project += 1

            # finish the most profitable project we can currently afford
            if heap:
                w -= heapq.heappop(heap)

        return w
