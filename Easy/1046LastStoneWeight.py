class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones_heap = [-stone for stone in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) >= 2:
            y = heapq.heappop(stones_heap)
            x = heapq.heappop(stones_heap)

            if x != y:
                heapq.heappush(stones_heap, y - x)

        return -heapq.heappop(stones_heap) if stones_heap else 0
