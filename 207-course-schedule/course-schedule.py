class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        registrar = defaultdict(list)
        for sub in prerequisites : registrar[sub[0]].append(sub[1])
        reminder = set()
        success = set()

        def dfs(course):
            
            if course in success: return True
            if course in reminder: return False

            reminder.add(course)
            for elems in registrar[course]:
                if not dfs(elems): return False

            success.add(course)
            reminder.remove(course)
            return True

        for crs,_ in prerequisites:
            if not dfs(crs): return False
            
        return True
