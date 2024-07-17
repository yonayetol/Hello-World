class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_hash = {}
        for i,pair in enumerate(points):
            distance = (pair[0]**2 + pair[1]**2)**0.5
            distance_hash[i] = distance
        #Now our distance_hash contains the distance of points as values and their indexes as keys 
        sorted_hash = sorted(distance_hash.items(),key=lambda x: x[1])
        # now sorted_hash has values in increasing order but the index of that distance is not altered
        final = []
        for pair in sorted_hash:
            i = pair[0]# remember i, is not altered and it is the index of the point in 'points'
            final.append(points[i])
            if len(final) == k:
                break
        return final