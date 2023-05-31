class UndergroundSystem:

    def __init__(self):
        self.last_checked_in = dict()
        self.average_time = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.last_checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        last_station, last_time = self.last_checked_in[id]
        prev_time_sum, prev_count = self.average_time[(last_station, stationName)]

        self.average_time[(last_station, stationName)][0] += t - last_time
        self.average_time[(last_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_sum, count = self.average_time[(startStation, endStation)]
        return time_sum / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
