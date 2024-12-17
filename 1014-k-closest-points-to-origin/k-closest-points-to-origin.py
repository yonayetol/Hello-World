class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_d_to_i = [[(lambda x,y:((x**2)+(y**2))**0.5)(points[i][0],points[i][1]),i] for i in range(len(points))]
        heapify(new_d_to_i)
        new_list = []
        for i in range(k):
            new_list.append(points[heappop(new_d_to_i)[1]])
        return new_list