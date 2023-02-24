# we are basically trying to make the max and min values of the list to be as close as possible
# we can only make even numbers smaller and odd numbers greater
# we have to multiply all odd numbers by 2
# because while small numbers will get bigger - the big ones can go back to being smaller
# minimazing the deviation

# extremely hard to come up with - I would not be able to do it without outside resources
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        # establish the priority queue and the smallest number in it
        min_val, min_deviation, heap = float('inf'), float('inf'), []
        for num in nums:
            if num % 2 == 0:
                heapq.heappush(heap, -num)
                min_val = min(min_val, num)
            else:
                heapq.heappush(heap, -num * 2)
                min_val = min(min_val, num * 2)

        # make next biggest numbers smaller and smaller as long as you can (until it's odd)
        while True:
            cur_max_val = -heapq.heappop(heap)
            min_deviation = min(min_deviation, cur_max_val - min_val)

            if cur_max_val % 2 != 0: break

            cur_max_val //= 2
            min_val = min(min_val, cur_max_val)
            heapq.heappush(heap, -cur_max_val)

        return min_deviation
