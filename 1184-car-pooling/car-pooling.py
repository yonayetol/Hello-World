class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
# person  from    to #   _0_  _1_  _2_  _3_   _4_  _5_   _6_   _7_   _8_    _9_  
#   3      2       7 #             3                          ^(-3)^
#   8      3       9 #                  8                                    ^-8^
#   3      7       9 #                                         3             ^-3^

        prefix_arr = [0]*1001
        for trip in trips:
            person, starting, the_end = trip[0],trip[1],trip[2]
            prefix_arr[starting] += person
            prefix_arr[the_end] -= person
            
        # let's sum things up and simultaneously check incase we have passed the capacity we gotta stop there
        if prefix_arr[0] > capacity:
            return False    # since we are gonna begin from 1, we need to check for the first one

        for i in range(1,1001):
            prefix_arr[i] += prefix_arr[i-1]
            if prefix_arr[i] > capacity:
                return False
        return True