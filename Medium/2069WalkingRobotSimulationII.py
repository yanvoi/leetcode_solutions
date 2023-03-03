# we can do it this way because the robot only walks on the edges and (width, height >= 2)
class Robot:

    def __init__(self, width: int, height: int):
        self.position = 0
        self.information = [[0, 0, 'South']]

        for x in range(1, width):
            self.information.append([x, 0, 'East'])

        for y in range(1, height):
            self.information.append([width - 1, y, 'North'])

        for x in range(width - 2, -1, -1):
            self.information.append([x, height - 1, 'West'])

        for y in range(height - 2, 0, -1):
            self.information.append([0, y, 'South'])
        

    def step(self, num: int) -> None:
        self.position += num


    def getPos(self) -> List[int]:
        return self.information[self.position % len(self.information)][:2]


    def getDir(self) -> str:
        return self.information[self.position % len(self.information)][2] if self.position else 'East'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
