class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #return the index of the peak
        #peak is where item before and after it are less than it
        
        i = 0
        
        while i != len(A) - 1:
            if i == 0:
                if A[i] > A[i+1]:
                    return 0
            else:
                if A[i-1] < A[i] > A[i+1]:
                    return i
            i = i + 1
