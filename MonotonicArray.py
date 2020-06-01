class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1 or len(A) == 2:
            return True
        
        else:
            i = 0
            while i != len(A) - 1:
                if A[i] == A[i + 1]:
                    i = i + 1
                elif A[i] > A[i+1]:
                    #mono decreasing
                    while i != len(A) - 1:
                        if A[i] > A[i+1]:
                            i = i + 1
                        elif A[i] == A[i+1]:
                            i = i + 1
                        else: return False
                else:
                    #mono increasing
                    while i != len(A) - 1:
                        if A[i] < A[i+1]:
                            i = i + 1
                        elif A[i] == A[i+1]:
                            i = i + 1
                        else: return False
            return True
