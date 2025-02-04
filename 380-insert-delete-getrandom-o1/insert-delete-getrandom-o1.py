from random import randint
class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.list_elems = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.list_elems)
        self.list_elems.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        removed = self.index_map[val]
        self.index_map[self.list_elems[-1]] = removed

        self.list_elems[removed],self.list_elems[-1] = self.list_elems[-1],self.list_elems[removed]

        self.list_elems.pop()
        del self.index_map[val]
        return True
    def getRandom(self) -> int:
        index = randint(0, len(self.list_elems) - 1)
        return self.list_elems[index]
