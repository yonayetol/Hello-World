class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_chem,left,right = 0,0,len(skill)-1
        team_potential = skill[0] + skill[-1]

        while left < right:
            if skill[left] + skill[right] == team_potential:
                total_chem += skill[left] * skill[right]
            else:
                return -1
            left += 1
            right -= 1
        return total_chem