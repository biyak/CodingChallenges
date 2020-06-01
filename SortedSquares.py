class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares = []
        
        for i in A:
            squares = squares + [i**2]
            
        squares.sort()
        
        return squares
