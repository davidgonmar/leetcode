class MyHashSet:

    def __init__(self):
        self.bucket = [[]] * 100

    def add(self, key: int) -> None:
       if not self.contains(key):
           self.bucket[key % 100].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.bucket[key % 100].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % 100
        return key in self.bucket[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)