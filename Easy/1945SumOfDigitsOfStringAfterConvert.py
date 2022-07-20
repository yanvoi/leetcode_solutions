class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def add_digits(number):
            
            sum = 0
            while number > 0:
                sum += number % 10
                number = number // 10
                
            return sum
        
        # creating a dictionary so we can assign a value to each letter in the alphabet
        chars = 'abcdefghijklmnopqrstuvwxyz'
        values = dict()
        i = 1
        
        for letter in chars:
            values[letter] = i
            i += 1
            
        # replacing letters with values and converting the string to int
        for letter in s:
            s = s.replace(letter, str(values[letter]))
            
        s = int(s)
        
        # adding digits of the number k times
        for i in range(k):
            s = add_digits(s)
            
        return s
        
