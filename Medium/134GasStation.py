class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force solution wastes a lot of time by checking
        # the same options that we already know fail

        start = surplus = total_surplus = 0
        for i in range(len(gas)):
            # total surplus will tell us if it's possible to make a full circle at all
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]

            # this means that the last starting point cannot be the answer
            if surplus < 0:
                surplus = 0
                start = i + 1

        return start if total_surplus >= 0 else -1
