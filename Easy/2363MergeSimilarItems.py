class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weight_of_value = [0] * 1001
        for item, weight in items1 + items2:
            weight_of_value[item] += weight

        return [[value, weight] for value, weight in enumerate(weight_of_value) if weight]
