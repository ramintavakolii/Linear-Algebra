import numpy as np
# import sys

def mul(A,B):
    lA = list(np.shape(A))
    lB = list(np.shape(B))

    # print(type(lA))
    # lA[1] equal to number of column for matrix A
    # lB[0] equal to number of row for matrix B

    if(lA[1]!= lB[0]):
        return []
    
    # Making a lA[0] by lB[1] matrix
    c =  [[0]*lB[1] for i in range(lA[0])]    
    # print('c = ',c)

    for i in range(lA[0]):
        for j in range(lB[1]):
            
            c[i][j] = sum([a*b for a,b in zip((A[i][:]),([row[j] for row in B]))])
            # print(list(zip((A[i][:]),([row[j] for row in B]))))
            # print(list([a*b for a,b in zip((A[i][:]),([row[j] for row in B]))]))
    return c

# test the function
P = [[0, 1, 0],
     [1, 0, 0],
     [0, 0, 1]]

B = [[1, 1, 0],
     [0, 2, 3],
     [9, 0, 3]]

C = [[1, 2],
    [3, 1.5],
    [0, 5/2.0]]

print(mul(P,B))
print(mul(B,P))
print(mul(P,C))