class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # creating a dictionary of how many times each number appears in the array
        h = dict()
        for num in nums:
            h[num] = h.get(num, 0) + 1
                
        # creating a dictionary of which elements appeared x times
        freq = dict()
        for el in h:
            freq[h[el]] = freq.get(h[el], []) + [el]
                
        # checking from the biggest possible frequency to the lowest
        ans = []
        for i in range(len(nums), 0, -1):
            if i in freq:
                
                for x in freq[i]:
                    ans.append(x)
                if len(ans) >= k:
                    return ans[:k]
                    
        return ans[:k]
        
