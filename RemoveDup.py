class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)== 1:
            return 1
        
        i=0
        j=1
        
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else: 
                i = i + 1
                j = j + 1
        return len(nums)
    
    def removeSecondDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        
        i=0
        j=1
        repeat = 0
        
        while j < len(nums):
            if nums[i] == nums[j] and repeat == 0:
                #First recurrance, is ok
                repeat = 1
                i = i + 1
                j = j + 1
            elif nums[i] == nums[j] and repeat == 1:
                nums.pop(j)
            else:
                repeat = 0
                i = i + 1
                j = j + 1
        return len(nums)
