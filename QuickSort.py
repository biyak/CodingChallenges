class QuickSort:
    def sortArray(nums):
        #identify beginning and end of array
        right = nums[len(nums)-1]
        left = nums[0]
        quickSort(nums, left, right)
        

    def quickSort(nums, left, right):
        if left >= right:
            #If the left index is greater than or equal to right
            #We know we've broken down the array into the smallest
            #pieces :P
            return 
        
        #Pick a pivot 
        pivot = len(nums)//2
        
        partindex = partition(nums, pivot, left, right)
        
        quickSort(nums, left, partindex -1)
        quickSort(nums, partindex, right)

    def partition(nums, pivot, left, right):
        while left <= right:
            while nums[left] < pivot:
                left = left + 1
            while nums[right] > pivot:
                right = right - 1
            
            if left <= right:
                l = nums[left]
                r = nums[right]
                nums[right] = l
                nums[left] = r
        return left

nums =[5,2,3,1]
sortArray(nums)
