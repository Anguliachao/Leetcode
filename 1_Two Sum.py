#my Python version
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i,item in enumerate(nums):
            nums_dict[item] = i
        for j in range(len(nums)):
            if target-nums[j] in nums_dict and nums_dict[target-nums[j]] != j:
                return [j,nums_dict[target-nums[j]]]
                
#optimized Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_dict:
                return [i,nums_dict[target-nums[i]]]
            else:
                nums_dict[nums[i]] = i

