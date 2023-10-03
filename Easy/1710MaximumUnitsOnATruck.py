class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        for num, units in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            toLoad = min(num, truckSize)
            answer += max(0, toLoad) * units
            truckSize -= toLoad

        return answer
