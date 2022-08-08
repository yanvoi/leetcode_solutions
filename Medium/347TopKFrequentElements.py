class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = dict()
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
                
        freq = dict()
        for el in h:
            if h[el] in freq:
                freq[h[el]].append(el)
            else:
                freq[h[el]] = [el]
                
        ans = []
        for i in range(len(nums), 0, -1):
            if i in freq:
                
                for x in freq[i]:
                    ans.append(x)
                if len(ans) >= k:
                    return ans[:k]
                    
        return ans[:k]
        
