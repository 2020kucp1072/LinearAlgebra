'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : matrix and vector multiplication

'''
import numpy as np
 
def vect_matrix_multi(X,Y):
    """
    Description:
    
      Multiplies a matrix by a vector.
    
    Parameters:
    
      - matrix: Input matrix (2D list)
      - vector: Input vector (1D list)
    
    Returns:
      - result: Resulting vector after multiplication (1D list)
      
    """
    row,col = X.shape
    result = np.zeros((row),dtype=int)
    
    for j in range(col):
        sum =0
        for i in range(row):
            sum = sum+ X[i,j]*Y[i]
        result[j]=sum
    
    return result



def main():
    
    #  main function
    
    X = np.array([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
    Y = np.array([1, 2, 3])

    Z= vect_matrix_multi(X,Y)
    print(Z)


if __name__=="__main__":
    main()