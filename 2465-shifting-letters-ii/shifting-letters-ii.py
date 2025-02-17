class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        my_array = [0]*(len(s))
        s = list(s)

        for left,right,direct in shifts:
            if direct:
                my_array[left] += 1
                if right+1 < len(s):
                    my_array[right+1] -= 1
            else:
                my_array[left] -= 1
                if right+1 < len(s):
                    my_array[right+1] += 1

        for i in range(1,len(my_array)):
            my_array[i] += my_array[i-1]

        for i in range(len(my_array)):
            place = ord(s[i]) - 97 + my_array[i]
            s[i] = chr(place%26 + 97)
        return "".join(s)