class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps, water = 0, capacity

        for index, needed_water in enumerate(plants):
            # it means we need to go back and refill our watering can
            if water < needed_water:
                steps += 2 * index
                water = capacity

            steps += 1
            water -= needed_water

        return steps
