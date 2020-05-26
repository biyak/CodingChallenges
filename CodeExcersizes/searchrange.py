
def searchrange(nums, target):
    #Find the starting and ending point of a target value in an array
    #Ex. find start and end of target = 8 in nums = [1,2,3,3,7,8,8,8,10,10]
    #Ans: return [5,7]
    print(nums)
    ind = helper(nums, target)

    print(ind)

    if ind == -1:
        return [-1,-1]

    else:
        start = ind
        end = ind
        while nums[start] == target and start != 0:
            start = start - 1
        while nums[end] == target and end != len(nums):
            end = end + 1
    end = end - 1
    return [start, end]

def helper(nums, target):
    mid = len(nums)//2

    if len(nums) == 0:
        return -1

    elif nums[mid] == target:
        print(nums[mid])
        return mid
    
    elif nums[mid] < target: #move -->
        nums = nums[mid+1:len(nums)] #Cut array from middle to end (half)
        print(nums)
        return helper(nums, target)
        
    elif nums[mid] > target: #move <--
        nums = nums[0: mid]
        print(nums)
        return helper(nums, target)
        

nums = [1,2,3,3,4,5]

A = searchrange(nums, 5)

print(A)
