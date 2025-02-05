class FrequencyTracker:

    def __init__(self):
        self.elem_count = Counter()
        self.count_who = defaultdict(set)

    def add(self, number: int) -> None:
        ind = self.elem_count[number]
        self.count_who[ind].discard(number)
        if len(self.count_who[ind]) == 0:
            del self.count_who[ind]

        self.elem_count[number] += 1
        self.count_who[self.elem_count[number]].add(number)

    
    def deleteOne(self, number: int) -> None:
        if number in self.elem_count:
            count = self.elem_count[number]

            self.count_who[count].remove(number)
            if len(self.count_who[count]) == 0:
                del self.count_who[count]
                
            self.elem_count[number] -= 1
            if self.elem_count[number] == 0:
                del self.elem_count[number]
            else:# adding to a new set with its corresponding set
                self.count_who[count-1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.count_who:
            return True
        return False