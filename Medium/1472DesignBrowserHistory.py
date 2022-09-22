class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current_page+1] + [url]
        self.current_page += 1

    def back(self, steps: int) -> str:
        if steps >= self.current_page + 1:
            self.current_page = 0
            return self.history[0]
        
        self.current_page -= steps
        return self.history[self.current_page]

    def forward(self, steps: int) -> str:
        if len(self.history) - self.current_page <= steps:
            self.current_page = len(self.history) - 1
            return self.history[-1]
        
        self.current_page += steps
        return self.history[self.current_page]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
