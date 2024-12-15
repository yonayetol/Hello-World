from heapq import heappush,heappop,heapify
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        my_dict = []
        for j in range(len(classes)):
            i = classes[j]
            predict = (i[0]+1)/(i[1]+1) - (i[0])/(i[1])
            heappush(my_dict,[-predict,j])
        for _ in range(extraStudents):
            ind = heappop(my_dict)[1]
            classes[ind][0] += 1
            classes[ind][1] += 1
            i = classes[ind]
            predict = (i[0]+1)/(i[1]+1) - (i[0])/(i[1])
            heappush(my_dict,[-predict,ind])
        answer = 0
        for i in classes:
            answer += i[0]/i[1]
        return answer/len(classes)