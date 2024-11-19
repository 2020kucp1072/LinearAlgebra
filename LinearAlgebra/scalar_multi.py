'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : scalar muliplication

'''
import numpy as np
 
def scalar_muliplication(X,Y):
    """
    Description:
    
       Multiplies a matrix by a scalar value.
    
    Parameters:
    
      - matrix: Input matrix (2D list)
      - scalar: Scalar value to multiply (int or float)
    
    Returns:
    
        - result: Matrix after scalar multiplication (2D list)
    """
    
    return Y*X

  


def main():
    
    #  main function
    
    X = np.array([[12,7,3], [4 ,5,6], [7 ,8,9]]) 
    Y = 9
    
    Z= scalar_muliplication(X,Y)
    print(Z)


if __name__=="__main__":
    main()