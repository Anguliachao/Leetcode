class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        dp = [0]*length
        if length<3:
            return 0
        if A[2]-A[1] == A[1]-A[0]:
            dp[2] = 1
        count = dp[2]
        for i in range(3,length):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1
            count+=dp[i]
        print(dp)
        return sum(dp)
#https://leetcode.com/problems/arithmetic-slices/discuss/90093/3ms-C%2B%2B-Standard-DP-Solution-with-Very-Detailed-Explanation
#这题难点在于将题目转化为DP问题，如果a[i-2],a[i-1],a[i]为一个序列，那么可以看做序列结束于a[i-1]，之后加上的a[i]也一定是arithmetic的。
