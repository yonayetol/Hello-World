class ProductOfNumbers:

    def __init__(self):
      self.nums = []
      self.their_pro = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            ptr = len(self.their_pro)-1
            while ptr > -1 and self.their_pro[ptr] != 0:
                self.their_pro[ptr] = 0
                ptr -= 1
            self.their_pro.append(0)# for 0 lets put 1
        else:
            if self.their_pro and self.their_pro[-1] != 0:
                self.their_pro.append(self.their_pro[-1]*num)
            else:
                self.their_pro.append(num)
                
    def getProduct(self, k: int) -> int:
        if k == len(self.their_pro):
            if self.their_pro[0] == 0:
                return 0
            return self.their_pro[-1]
        else:
            if self.their_pro[-k-1] == 0:
                past = 1
                if self.their_pro[-k] == 0:
                    return 0
            else:
                past = self.their_pro[-k-1]
        return int(self.their_pro[-1]//past)