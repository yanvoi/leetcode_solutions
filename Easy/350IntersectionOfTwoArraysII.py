class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        first = dict()
        second = dict()
        
        for el in nums1:
            if el in first:
                first[el] += 1
            else:
                first[el] = 1
                
        for el in nums2:
            if el in second:
                second[el] += 1
            else:
                second[el] = 1
            
        answer = []
        for element in first:
            if element in second:
                for i in range(min(first[element], second[element])):
                    answer.append(element)
                    
        return answer
        
