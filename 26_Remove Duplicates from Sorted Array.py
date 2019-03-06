My answer:
        def removeDuplicates(nums):
    del_idx = []
    for i in range(len(nums)):
        if i in del_idx:
            continue
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                del_idx.append(j)
    nums = [x for idx,x in enumerate(nums) if idx not in del_idx]
    #for x in del_idx:
    #    del nums[x]
    return nums    
nn = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(nn)

Python version 
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
if not nums:return 0
len_list = len(nums)
i = 0
for j in range(1,len(nums)):
   if nums[i] != nums[j]:
   nums[i+1] = nums[j]
   i += 1
 
C++ version
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = nums.size();
        int slow = 0;
        for(fast=0;fast<l;++fast)
            if nums[slow]!=nums[fast]{
                nums[++slow] = nums[fast];
                    }
        return fast+1;
            };
