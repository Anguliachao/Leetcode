###Python Version
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        pro = 0
        for i in range(1,l):
            if prices[i]-prices[i-1]>0:
                diff = prices[i]-prices[i-1]
                pro += diff
        return pro
        
###C++ Version
int maxProfit(vector<int> &prices) {
    ret = 0
    for(int i=1;i<prices.size();i++){
       if prices[i] - prices[i-1]>0:
           ret+=prices[i]-prices[i-1]
    }
    return ret
}
