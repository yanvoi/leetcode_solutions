class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        count = Counter(nums)
        answer = 0

        for num in count:
            # if k == 0 then we just need to check if an element appears more than once
            # if k > 0 then we check if there is a number x in the list that abs(num - x) == k
            if (k == 0 and count[num] > 1) or (k > 0 and num + k in count):
                answer += 1

        return answer
        
