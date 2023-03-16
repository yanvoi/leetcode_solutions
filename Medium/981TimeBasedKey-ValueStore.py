# read carefully what the get method is supposed to do!
class TimeMap:

    def __init__(self):
        self.by_key = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.by_key[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.by_key[key])

        while left < right:
            mid = (left + right) // 2
            if self.by_key[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return self.by_key[key][right - 1][1] if right else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
