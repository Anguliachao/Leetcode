#Python solution
class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        length = len(nums)
        if length<2:
            return 0
        sort_nums = sorted(nums)
        max_gap = 0
        for i in range(length-1):
            cur_gap  = sort_nums[i+1] - sort_nums[i]
            if cur_gap>max_gap:
                max_gap = cur_gap
        return max_gap

#C++ solution
class Solution {
public:
    /**
     * @param nums: an array of integers
     * @return: the maximun difference
     */
    int maximumGap(vector<int> &nums) {
        // write your code here
        if( nums.empty() || nums.size() <2)
            return 0;
        int maxGap = 0;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++)
            maxGap = max(nums[i+1]-nums[i],maxGap);
    
        return maxGap;
    }
};

#分析：
#本题难点在于如何排序乱序数组，内嵌排序算法的复杂度为nlogn，但是radix sorting 和 buket sorting等方法能够达到n的时间复杂度。（我的答案都是nlogn的解法）
#n复杂度解法参考 ： https://leetcode.com/articles/maximum-gap/
