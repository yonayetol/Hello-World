class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right,needed_boats = 0,len(people)-1,0

        while left <= right:
            if people[left] + people[right] >= limit:
                needed_boats += 1
                if people[left] + people[right] == limit: 
                    left += 1
                right -= 1
            else:
                left += 1
                right -= 1
                needed_boats += 1

        return needed_boats
