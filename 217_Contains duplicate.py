###Python version
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #i = 0
        #length = len(nums)
        #copy_nums = []
        #for j in range(0,length):
        #    for i in range(j+1,length):
        #        if nums[j] == nums[i]:
        #            return True
        #return False
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
            
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        copy_nums = []
        
        for j in nums:
            if j in copy_nums:
                return True
            copy_nums.append(j)
        return False
        
 ###C++
 class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return set<int>(nums.begin(),nums.end()).size() != nums.size();
    }
};
