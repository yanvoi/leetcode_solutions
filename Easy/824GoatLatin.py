class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        words = sentence.split()
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        index = 1
        
        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i] = words[i] + 'ma'
            else:
                words[i] = (words[i])[1:] + words[i][0] + 'ma'
                
            words[i] = words[i] + 'a' * index
            index += 1
        
        return ' '.join(words)
        
