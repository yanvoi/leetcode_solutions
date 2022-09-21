class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum = 0
        for num in nums:
            if num % 2 == 0: even_sum += num
                
        answer = []
        for val, index in queries:
            if nums[index] % 2 == 0 and val % 2 == 0:
                nums[index] += val
                even_sum += val
            elif nums[index] % 2 == 0:
                even_sum -= nums[index]
                nums[index] += val
            elif val % 2 == 0:
                nums[index] += val
            else:
                nums[index] += val
                even_sum += nums[index]
                
            answer.append(even_sum)
            
        return answer
        
