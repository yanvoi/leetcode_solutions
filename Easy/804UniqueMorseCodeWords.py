class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s = set()
        
        for word in words:
            trans = ''
            for letter in word:
                trans = trans + morse[ord(letter) - 97]
            s.add(trans)
            
        return len(s)
    
