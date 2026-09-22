class MyHashSet:

    def hash(self, key) -> int:
        return key % 1000

    def __init__(self):
        self.lst=[[] for _ in range(1000)]

    def add(self, key: int) -> None:
        i=self.hash(key)
        if not key in self.lst[i]:
            self.lst[i].append(key) 
            return
        else:
            return 

    def remove(self, key: int) -> None:
        i=self.hash(key)
        for j in range(len(self.lst[i])):
            if self.lst[i][j]==key:
                del self.lst[i][j]
                return
    
    def contains(self, key: int) -> bool:
        i=self.hash(key)
        if key in self.lst[i]:
            return True
        else:
            return False
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)