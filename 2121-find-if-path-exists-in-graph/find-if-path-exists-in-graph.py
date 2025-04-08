class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        grids = defaultdict(list)
        for sub in edges:
            grids[sub[0]].append(sub[1])
            grids[sub[1]].append(sub[0])
        
        reminder = set()
        def cooker(source):
            if source == destination: return True           # 0:1  1:2   2:0
                
            if source in reminder: return False

            reminder.add(source)
            # print(source, "added")

            for option in grids[source]:
                if cooker(option): return True

            return False


        return cooker(source)