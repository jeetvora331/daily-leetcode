class MyHashSet:

    def __init__(self):
        self.dict = {}
        

    def add(self, key: int) -> None:
        self.dict[key]  = 1

    def remove(self, key: int) -> None:
        self.dict[key] = 0

    def contains(self, key: int) -> bool:
        temp = self.dict.get(key , 0)
        return temp != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)