##Python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(int(length/2)):
            matrix[i],matrix[length-1-i] = matrix[length-1-i],matrix[i]
        for m in range(length):
            for n in range(m):
                matrix[m][n],matrix[n][m] = matrix[n][m],matrix[m][n]
##C++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (!matrix.size()) return;
        const int N = matrix.size();
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N / 2; j ++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][N - j - 1];
                matrix[i][N - j - 1] = tmp;
            }
        }
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N - i; j ++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[N - j - 1][N - i - 1];
                matrix[N - j - 1][N - i - 1] = tmp;
            }
        }
    }
};
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/79451733 
版权声明：本文为博主原创文章，转载请附上博文链接！
