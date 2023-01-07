class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.last_int = 0
        self.last_consecutive_count = 0
        

    def consec(self, num: int) -> bool:
        if num == self.last_int:
            self.last_consecutive_count += 1
        else:
            self.last_int = num
            self.last_consecutive_count = 1
            
        return num == self.value and self.last_consecutive_count >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
