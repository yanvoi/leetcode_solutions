# bucket sort + left sum == O(n) time && O(1) space
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        # bucket sort by age
        buckets = [0] * 121
        for age in ages:
            buckets[age] += 1

        # left sum of the buckets list
        for age in range(1, 121):
            buckets[age] += buckets[age - 1]

        # count the number of invites
        answer = 0
        for age in range(1, 121):
            age_cont = buckets[age] - buckets[age - 1]
            too_young_age = math.floor(0.5 * age + 7)
            too_young_count = buckets[too_young_age]

            if too_young_age  >= age: continue
            answer += age_cont * (buckets[age - 1] - too_young_count)
            answer += age_cont * (age_cont - 1)

        return answer
