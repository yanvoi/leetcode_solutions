class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        sequences, answer = set(), set()
        
        for i in range(len(s)):
            sequence = s[i:i+10]
            if sequence in sequences:
                answer.add(sequence)
            sequences.add(sequence)
        
        return list(answer)
        
