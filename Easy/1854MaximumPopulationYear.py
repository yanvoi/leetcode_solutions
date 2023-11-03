# O(n) time, O(1) space
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101
        offset = 1950
        for birth, death in logs:
            population[birth - offset] += 1
            population[death - offset] -= 1

        for i in range(1, len(population)):
            population[i] += population[i - 1]

        return max([i for i in range(len(population))], key=lambda x: population[x]) + offset
        
