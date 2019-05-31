class Solution:
    def maxKilledEnemies(self,grid):
        #refer links:
        #https://blog.csdn.net/qq508618087/article/details/51705806
        #https://www.cnblogs.com/grandyang/p/5599289.html
        if not grid:
            return 0
        #length of row , column
        row,col = len(grid),len(grid[0])
        rowCnt = 0
        colCnt = [0 for x in range(col)]
        res = 0
    
        for i in range(row):
            for j in range(col):
                #if first row or previous row is Wall, we start search
                if i==0 or grid[i-1][j]=='W':
                    colCnt[j] = 0
                    for m in range(i, row):
                        # if current grid is not Wall
                        if grid[m][j] != 'W':
                            colCnt[j] += (grid[m][j] == 'E')
                        else:
                            break
    
    
                #if first col or previous col is Wall, we start search
                if j==0 or grid[i][j-1]=='W':
                    rowCnt = 0
                    # we search to the end of row
                    # search till the end of col
                    for n in range(j, col):
                        if grid[i][n] != 'W':
                            rowCnt += (grid[i][n] == 'E')
                        else:
                            break
                #update the best location
                if grid[i][j] == '0':
                    res = max(res,rowCnt+colCnt[j])
        return res
