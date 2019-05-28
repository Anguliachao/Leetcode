#https://leetcode.com/problems/super-ugly-number/discuss/169815/Python-DP-solution-beats-93.7-extremely-detailed-explanation
class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        size = len(primes)
        ugly,dp,index,ugly_nums = 1,[1],[0]*size,[1]*size
        for i in range(1,n):
            #compute possibly ugly numbers
            for j in range(0,size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]]*primes[j]
                    index[j] += 1
                
            #get the min
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]
