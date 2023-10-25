# O(n) time, O(n) space
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        press_time = defaultdict(int)
        if releaseTimes: press_time[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            press_time[keysPressed[i]] = max(press_time[keysPressed[i]], releaseTimes[i] - releaseTimes[i - 1])

        return max([key for key in press_time], key=lambda x: (press_time[x], x))
