class RandomizedSet:
    def __init__(self):
        self.a, self.d = [], {}


    def insert(self, v: int) -> bool:
        if v in self.d:
            return False

        self.d[v] = len(self.a)
        self.a.append(v)

        return True
        

    def remove(self, v: int) -> bool:
        if v not in self.d:
            return False

        e, i = self.a.pop(), self.d.pop(v)
        if i < len(self.a):
            self.a[i], self.d[e] = e, i
        
        return True
        

    def getRandom(self) -> int:
        return choice(self.a)