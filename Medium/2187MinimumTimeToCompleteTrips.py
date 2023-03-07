# binary search but tricky
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        left, right = min(time), min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2
            if sum(mid // bus_trip for bus_trip in time) < totalTrips:
                left = mid + 1
            else:
                right = mid

        return left
