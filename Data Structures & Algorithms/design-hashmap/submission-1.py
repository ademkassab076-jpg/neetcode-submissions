class MyHashMap:
    def hash(self, key):
        return key%1000

    def __init__(self):
        self.lst=[[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        i=self.hash(key)
        for x in self.lst[i]:
            if x[0]==key:
                x[1]=value
                return
        self.lst[i].append([key,value])
    def get(self, key: int) -> int:
        i=self.hash(key)
        for x in self.lst[i]:
            if x[0]==key:
                return x[1]
        return -1

    def remove(self, key: int) -> None:
        i=self.hash(key)
        for j,x in enumerate (self.lst[i]):
            if x[0]==key:
                del self.lst[i][j]
                return 




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)