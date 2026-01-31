class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        newList, visited = [], set()
        for char in letters:
            if char not in visited:
                newList.append(char)
                visited.add(char)
            
        left , right, target_val = 0 , len(newList)-1, ord(target)
        while True:
            mid = (left + right)//2           
            mid_val = ord(newList[mid]) 
            if left == right: 
                if mid_val > target_val: 
                    return newList[mid] if mid < len(newList) else newList[0]
                else:
                    return newList[mid+1] if mid+1 < len(newList) else newList[0]
            if mid_val > target_val: right = mid-1
            else: left = mid+1
            if left > right: return newList[mid] if mid < len(newList) else newList[0]
