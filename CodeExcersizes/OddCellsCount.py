from typing import List

def oddCells(n, m, indices):
    A = [[0]*m]*n #solution matrix
    
    for each in indices:
        ri = each[0]
        ci = each[1]
        
        #Access the row
        for i in range(0, m):
            A[ri][i] = A[ri][i]  + 1
            print(ri)
            print(i)
            print(A)
        #Access the column
            
n = 2
m = 3
indices = [[0,1],[1,1]]

oddCells(n, m, indices)
