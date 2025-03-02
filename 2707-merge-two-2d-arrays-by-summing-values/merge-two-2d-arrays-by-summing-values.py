class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # let's do it in two ways, short one and the long one
        # short first 
        my_dict = {key: value for key, value in nums1}
        for key, value in nums2:
            my_dict[key] = value + my_dict.get(key, 0)
        return sorted([[key, value] for key, value in my_dict.items()], key = lambda x: x[0])
        
        # then the long but more efficient one 
        ptr1 = ptr2 = 0
        answer = []
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1][0] < nums2[ptr2][0]:
                answer.append(nums1[ptr1])
                ptr1 += 1
            elif nums1[ptr1][0] == nums2[ptr2][0]:
                answer.append([nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
            else:
                answer.append(nums2[ptr2])
                ptr2 += 1
        # incase there are some numbers left lets catch them
        answer += nums1[ptr1:]
        answer += nums2[ptr2:] 

        return answer

