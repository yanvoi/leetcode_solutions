class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        # creating a dictionary of which elements appeared x times
        frequencies = defaultdict(list)
        for num, freq in counter.items():
            frequencies[freq].append(num)
                
        answer = []
        # checking from the highest possible frequency to the lowest
        for freq in range(len(nums), 0, -1):
            for num in frequencies[freq]:
                answer.append(num)
            if len(answer) >= k:
                return answer[:k]
                    
        return answer[:k]
        
