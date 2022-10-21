class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        # counting how many times each number appears
        freq = dict()
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        # counting how many elements appear i-1 times
        frequencies = [0] * len(arr)
        for val in freq.values():
            frequencies[val-1] += 1
        
        # counting which number to delete from the most to least frequent
        # when we get the number of deleted elements we wanted, we return the count
        ans, deleted = 0, 0
        for i in range(len(frequencies) - 1, -1, -1):
            for j in range(frequencies[i]):
                deleted += i+1
                ans += 1
                
                if deleted >= len(arr) // 2: return ans
                
        return ans
        
