class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        leng = len(nums)
        if leng<2 or nums==None:
            return [0,0]
        #left pointer i and right pointer j 
        i=0
        j = i 
        while i < (leng-1):
            for j in range(i+1,leng):
                if nums[i]+nums[j] == target:
                    return [i+1,j+1]
                if nums[i]+nums[j] > target:
                    break
            i = i+1#move pointer forward
        return [0,0]
                    
