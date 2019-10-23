def maximumSum(arr):
    # Write your code here
    maxSum = 0
    
    maxSumNow = 0
    for i in arr:
        maxSumNow = maxSumNow + i
        if maxSumNow < 0:
            maxSumNow = 0
        elif (maxSum < maxSumNow): 
            maxSum = maxSumNow 

    return int(maxSum)
