class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left, basket = 0, defaultdict(int)

        for fruit in fruits:
            basket[fruit] += 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

        return len(fruits) - left

        # easy problem to understand but the solution is tricky
        # the gap between the right and the left pointer
        # represents the longest subarray with 2 different elements
