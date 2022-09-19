class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        
        self.big_ones = 0
        self.medium_ones = 0
        self.small_ones = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > self.big_ones:
                self.big_ones += 1
                return True
        elif carType == 2:
            if self.medium > self.medium_ones:
                self.medium_ones += 1
                return True
        else:
            if self.small > self.small_ones:
                self.small_ones += 1
                return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
