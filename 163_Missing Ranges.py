#Python 
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution(object):
    def findMissingRanges(self,nums,lower,upper):
        #extreme case , empty list
        if len(nums) <1:
            if upper>lower:
                return [str(lower)+'->'+str(upper)]
            else:
                return [str(lower)]
        #non empty list
        
        #create result list
        result = []
        #first element
        if nums[0] - lower >1:
            result.append(str(lower)+'->'+str(nums[0]-1))
        elif nums[0] - lower == 1:
            result.append(str(lower))
            
        #the rest gap
        for i in range(1,len(nums)):
            if nums[i-1]+1 != nums[i]:
                #only gaps 1
                if nums[i-1]+1 == nums[i] -1:
                    result.append(str(nums[i-1]+1))
                else:
                    result.append(str(nums[i-1]+1)+'->'+str(nums[i]-1))
                    
        if upper - nums[len(nums)-1] >1:
            result.append(str(nums[len(nums)-1]+1)+'->'+str(upper))
        elif upper - nums[len(nums)-1] ==1:
            result.append(str(upper))
            
        return result
    
