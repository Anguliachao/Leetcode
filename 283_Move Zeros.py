# The idea of move zeros resides in moving all non-zero elements to array front
#  Thus we introduce a index position to maintain non-zeros, others all zero
## Python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cc =0
        for i in nums:
            if i!=0:
                nums[cc] = i
                cc+=1
        for j in range(cc,len(nums)):
            nums[j] = 0
        
##C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                nums[j] = nums[i];
                j++;
            }
        }
        for(;j<nums.size();j++){
            nums[j] = 0;
        }
    }
};
