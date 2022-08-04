class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s1, e1 in self.bookings:
            # De Morgan's Law: not (e1 <= start or s1 >= end) becomes:
            if e1 > start and s1 < end:
                return False
        self.bookings.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
