#https://www.cnblogs.com/grandyang/p/9311385.html
#https://www.youtube.com/watch?v=mLTF2UXkd2o
#https://blog.csdn.net/magicbean2/article/details/79826617
#https://blog.csdn.net/fuxuemingzhu/article/details/83269027
#https://blog.csdn.net/fuxuemingzhu/article/details/83247054

#这道题的难度在于理解维护两个列表更新最小的交换次数
#一个no_swap列表，表明当前i项在不交换的情况下均能保持increasing
#一个swap列表，表明当前i-1项在不交换的情况下均能保持increasing
#存在说对角对比的情况，交换i-1对数据，能让i达到最优解，或者交换i对数据，能让i-1对达到最优解
#O(N) space solution
class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        # Write your code here
        length = len(A)
        if length<1:
            return 0
        #dp1 keeps no swap list 
        dp1 = [0]*length
        #dp2 keeps swap list 
        dp2 = [1]*length
        
        for i in range(1,length):
            dp1[i] = dp2[i] = length
            #if no swap , keeps in order
            if A[i-1]<A[i] and B[i-1]<B[i]:
                dp1[i] = dp1[i-1]
                dp2[i] = dp2[i-1]+1 
            #if swap, keeps in order
            if A[i-1]<B[i] and B[i-1]<A[i]:
                dp1[i] = min(dp1[i],dp2[i-1])
                dp2[i] = min(dp2[i],dp1[i-1]+1)
                
        return min(dp1[length-1],dp2[length-1])
