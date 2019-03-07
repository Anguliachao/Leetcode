
#http://liadbiz.github.io/leetcode-single-number-problems-summary/
###Python version
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return  2*sum(set(nums)) - sum(nums)
        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #return 2*sum(set(nums)) - sum(nums)
        result = 0
        for i in nums:
            result^=i
        return result        
        
  
###C++ version
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for(int x=0;x<nums.size();x++)
            result^=nums[x];
        return result;
    }
};
