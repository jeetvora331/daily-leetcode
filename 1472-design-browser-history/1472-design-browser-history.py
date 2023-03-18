class BrowserHistory:

    def __init__(self, homepage: str):
        self.backw = []
        self.forw = []
        self.backw.append(homepage)

    def visit(self, url: str) -> None:
        self.forw = []
        self.backw.append(url)

    def back (self, steps: int) -> str:
        while steps >0 and len(self.backw) > 1:
            self.forw.append(self.backw.pop())
            steps -=1
        
        return self.backw[-1]

    def forward(self, steps: int) -> str:
        while steps >0 and len(self.forw) > 0:
            self.backw.append(self.forw.pop())
            steps -=1
        
        return self.backw[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.self.backw(steps)
# param_3 = obj.forward(steps)