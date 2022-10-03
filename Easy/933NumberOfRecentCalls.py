class RecentCounter:

    def __init__(self):
        self.recent = collections.deque()
        

    def ping(self, t: int) -> int:
        self.recent.append(t)
        
        while self.recent[0] < t - 3000:
            self.recent.popleft()
        
        return len(self.recent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
