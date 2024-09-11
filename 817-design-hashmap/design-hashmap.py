class MyHashMap:

    def __init__(self):
        self.bucket = [{}] * 1000

    def hash(self, key):
        return key % 1000

    def put(self, key: int, value: int) -> None:
        self.bucket[self.hash(key)][key] = value

    def get(self, key: int) -> int:
        indiv = self.bucket[self.hash(key)]
        if key in indiv:
            return indiv[key]
        return -1

    def remove(self, key: int) -> None:
        indiv = self.bucket[self.hash(key)]
        if key in indiv:
            del indiv[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)