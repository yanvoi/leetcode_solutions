class Codec:

    def __init__(self):

        self.chars = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()QAZWSXEDCRFVTGBYHNUJMIKOLP'
        self.long_to_short = dict()
        self.short_to_long = dict()
        self.base = 'http://tinyurl.com/'


    def encode(self, longUrl: str) -> str:
        
        while longUrl not in self.long_to_short:
            code = ''.join(random.choice(self.chars) for _ in range(10))
            if code not in self.short_to_long:
                self.long_to_short[longUrl] = code
                self.short_to_long[code] = longUrl

        return self.base + self.long_to_short[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.short_to_long[shortUrl[len(self.base):]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
