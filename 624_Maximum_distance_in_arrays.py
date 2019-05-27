#Python solution:关键点在于保证最大元素和最小元素不是来自同一个list，之后动态更新当前数据尾元素与curMin的差值，curMax与当前数组头元素的差值，即可得到最大的差值
class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    https://www.jianshu.com/p/8cdf02a4d30a
    https://www.cnblogs.com/grandyang/p/7073343.html
    """
    def maxDiff(self, arrs):
        # write your code here
        res,curMin,curMax = 0,10000,-10000
        for arr in arrs:
            res = max(res,max(arr[-1]-curMin,curMax-arr[0]))
            curMin,curMax = min(curMin,arr[0]),max(arr[-1],curMax)
        return res
