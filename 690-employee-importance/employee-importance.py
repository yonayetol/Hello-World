"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinate = defaultdict(list)
        for person in employees:
            subordinate[person.id] = (person.importance, person.subordinates)
            
        answer = 0
        def goFor(id):
            nonlocal answer
            answer += subordinate[id][0]
            for person in subordinate[id][1]:
                goFor(person)
                
        goFor(id)
        return answer
