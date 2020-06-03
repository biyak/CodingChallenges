class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #min element is one that has a large lement before and after
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else: return nums[0]
        
        i = 0
        
        while i < len(nums):
            if i == 0:
                prev = nums[-1]
                after = nums[1]
                if prev > nums[i] and after > nums[i]:
                    #this is min bitch 
                    return nums[i]
                else: i = i + 1
                    
            elif i == len(nums)-1:
                prev = nums[i-1]
                after = nums[0]
                if prev > nums[i] and after > nums[i]:
                    return nums[i]
                else: i = i + 1
                    
            else:
                prev = nums[i-1]
                after = nums[i+1]
                if prev > nums[i] and after > nums[i]:
                    return nums[i]
                else: i = i + 1
        
