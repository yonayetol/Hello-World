class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        my_dict = {arr2[i]:i for i in range(len(arr2))}
        def mine(elem):
            if elem in my_dict:
                return my_dict[elem],elem
            return float('inf'),elem
        arr1.sort(key = mine)
        return arr1