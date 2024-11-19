'''
    @Author: VEMULA DILEEP
    @Date: 07-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 07-11-2024
    @Title : adding matrices

'''

import numpy as np


def adding_matrices(X,Y):
    
    """
    Adds two matrices element-wise.
    
    Parameters:
    - matrix1: First matrix (2D list)
    - matrix2: Second matrix (2D list)
    
    Returns:
    - result: Sum of the two matrices (2D list)
    """
    
    return X+Y



def main():
    
    X = np.array([[12,7,3], [4 ,5,6], [7 ,8,9]] )
    Y = np.array([[5,8,1], [6,7,3], [4,5,9]]) 
    
    Z = adding_matrices(X,Y)
    print(Z)


if __name__ == "__main__":
    main()