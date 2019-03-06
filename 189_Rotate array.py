#https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51462800
#https://blog.csdn.net/a2331046/article/details/52244690
#https://blog.csdn.net/crazy1235/article/details/85924613
###Python version
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        k = k%length
        self.reverse(nums,0,length-1)
        self.reverse(nums,k,length-1)
        self.reverse(nums,0,k-1)
        
    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
            
###C++ Version
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k%nums.size();
        int length = nums.size();
        reverse(nums,0,length-1);
        reverse(nums,k,length-1);
        reverse(nums,0,k-1);
    }
    void reverse(vector<int>& nums,int start,int end){
        int temp;
        while(start<end){
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
};
