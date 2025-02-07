class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = {}
        for i in range(len(list1)):
            list1_dict[list1[i]] = i
        
        little = float('inf')
        index_catcher = set()
        for i in range(len(list2)):
            if list2[i] in list1_dict:
                sum = i + list1_dict[list2[i]]
                if little >= sum:
                    if little > sum:
                        index_catcher.clear()
                    index_catcher.add(i)
                    little = sum
                print(sum)
        return [list2[i] for i in index_catcher]