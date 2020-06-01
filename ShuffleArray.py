import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = list(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.original
        self.original = list(self.original)
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        options = self.nums
        shuffled = []
        print(self.original)
        
        while len(options) != 0:
            index = random.randrange(len(options))
            
            shuffled.append(options[index])
            
            options.pop(index)
        
        self.nums = shuffled
        return shuffled
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
