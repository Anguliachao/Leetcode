#思路：动态规划，当前格子所有的path可能性取决于其左边邻居于上方邻居
#所以直接更新2D矩阵
#优化部分：a.仅由当前行与前一行更新种类
#         b.只用一行进行更新
#O(mn) solutions
def uniquePaths(self, m, n):
        dp = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        # write your code here
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
#O(n) solutions
def uniquePaths(self, m: int, n: int) -> int:
    cur = [1]*n
    for i in range(1,m):
        for j in range(1,n):
            cur[j]+=cur[j-1]
    return cur[-1]
            
#O(n) solutions
def uniquePaths(self, m: int, n: int) -> int:
        prev,cur = [1 ]*n,[1 ]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] = prev[j]+cur[j-1]
            cur,prev = prev,cur
        return prev[n-1]
