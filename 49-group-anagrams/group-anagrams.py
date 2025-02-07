class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for i in range(len(strs)):
            small_dict = [0]*26
            for j in strs[i]:
                small_dict[ord(j)-97] += 1

            for keyy,value in my_dict.items():
                if value[0] == small_dict:
                    my_dict[keyy][1].append(i)
                    break
            else:
                my_dict[strs[i]] = [small_dict,[i]]
        answer = []
        for keyy,value in my_dict.items():
            answer.append([strs[i] for i in value[1]])

        return answer