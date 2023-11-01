# 0 <= bound <= 10^6
# 2^20 > 10^6
# try all combinations for powers < 20
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_powers = [x ** power for power in range(20)]
        y_powers = [y ** power for power in range(20)]
        return list({x_p + y_p for x_p in x_powers for y_p in y_powers if x_p + y_p <= bound})
