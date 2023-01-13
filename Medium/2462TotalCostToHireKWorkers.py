class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        # add float('inf') to each of these so we avoid having empty heaps
        left = costs[:candidates] + [float('inf')]
        right = costs[max(candidates, len(costs) - candidates):] + [float('inf')]
        heapq.heapify(left)
        heapq.heapify(right)
        # indices of the next elements to add to each heap
        next_left, next_right = candidates, len(costs) - candidates - 1
        answer = 0

        for _ in range(k):
            if left and left[0] <= right[0]:
                answer += heapq.heappop(left)
                if next_left <= next_right:
                    heapq.heappush(left, costs[next_left])
                    next_left += 1
            else:
                answer += heapq.heappop(right)
                if next_left <= next_right:
                    heapq.heappush(right, costs[next_right])
                    next_right -= 1

        return answer
        
