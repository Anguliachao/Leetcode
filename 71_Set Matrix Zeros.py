#Python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False

        m = len(matrix)
        n = len(matrix[0])
        
        #whether first col has 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
        #whether first row has 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
        # in the matrix middle has 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0]=matrix[0][j] =0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] =0
        
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
