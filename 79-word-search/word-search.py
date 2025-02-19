class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols,rows = len(board[0]),len(board)
        reminder = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0) or (r>=rows or c>=cols) or (board[r][c]!=word[i]) or ((r,c) in reminder):
                return False

            reminder.add((r,c)) # let's catch this grid since it's done marvelous thing by passing these if-case
            tempo = (dfs(r+1,c,i+1,) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            reminder.remove((r,c)) #incase we weren't succesful using these grid after trying till the end

            return tempo
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False