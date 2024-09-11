class Solution:
    def exist(self, board,word):
        m = len(board)
        n = len(board[0])
        def dfs(i,j,idx,visited):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[idx] or (i,j) in visited:
                return False
            if board[i][j]==word[idx]:
                idx +=1
                if idx == len(word):
                    return True
            visited.add((i,j))
            if dfs(i-1,j,idx,visited) or dfs(i,j-1,idx,visited) or dfs(i+1,j,idx,visited) or dfs(i,j+1,idx,visited):
                return True
            visited.remove((i,j))
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0,set()):
                    return True
        return False
