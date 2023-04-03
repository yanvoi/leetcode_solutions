# group the heaviest person with the lighest person
# repeat untill all people are boarded
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        answer = 0
        left, right = 0, len(people) - 1

        while left <= right:
            # edge case: someone is so heavy they have to swim alone
            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1
            answer += 1

        return answer
        
