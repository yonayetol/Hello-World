class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        num = 0
        other = []
        for i in range(len(code)):
            other.append(0)
            print("for ",i)
            for j in range(abs(k)):
                ind = i+j+1
                if k < 0:
                    ind = i-j-1 # for negative increaments
                print("ind",ind)
                if abs(ind) >= len(code):
                    back = ind % len(code)
                    if k<0:
                        back *= -1
                    other[i] += code[back]
                    print("back is added ", back)
                else:
                    other[i] += code[ind]

        return other
