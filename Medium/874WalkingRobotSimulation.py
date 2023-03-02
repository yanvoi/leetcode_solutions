# it's just a simulation of the walking
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int: 

        # initizalizing needed variables
        x, y, turned, answer = 0, 0, 0, 0
        not_permitted = {tuple(obstacle) for obstacle in obstacles}
        # in order of turning right
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # loop over the commands
        for command in commands:
            # turn right
            if command == -1:
                turned = (turned + 1) % 4
            # turn left
            elif command == -2:
                turned = (turned - 1) % 4

            # move k steps
            else:
                x2, y2 = move[turned]

                while command and (x + x2, y + y2) not in not_permitted:
                    x, y = x + x2, y + y2
                    answer = max(answer, x ** 2 + y ** 2)
                    command -= 1

        return answer
