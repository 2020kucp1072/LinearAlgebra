'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : matrix and matrix multiplication

'''
import numpy as np
 
def mat_matrix_multi(X,Y):
    """
    Description:
    
      Multiplies a matrix by a matrix.
    
    Parameters:
    
      - matrix: Input matrix (2D list)
      - vector: Input vector (1D list)
    
    Returns:
      - result: Resulting matrix after multiplication(2D list)
      
    """
    row1,col1 = X.shape
    row2,col2 = Y.shape
    result = np.zeros((row1,col2),dtype=int)
    
    for i in range(row1):
        for j in range(col2):
           sum =0
           for z in range(col1):
             sum = sum+ X[i,z]*Y[z,j]
           result[i,j]=sum
    
    return result



def main():
    
    #  main function
    
    X = np.array([[12,7,3], [4 ,5,6], [7 ,8,9]]) 
    Y = np.array([[5,8,1], [6,7,3], [4,5,9]]) 

    Z= mat_matrix_multi(X,Y)
    print(Z)


if __name__=="__main__":
    main()