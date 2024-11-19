'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : inverse of matrix

'''
import numpy as np
 
def inv2_matrix(X):
    """
    Description:
    
      inverse of matrix
    
    Parameters:
    
      - matrix: Input matrix 
      
    
    Returns:
      - result: inverse matrix
      
    """
    if np.linalg.det(X)!=0:    
     result =np.linalg.inv(X) 
     
    return result



def main():
    
    #  main function
    
    Y = np.array([[5,8,1], [6,7,3], [4,5,9]]) 
    Z= inv2_matrix(Y)
    print(Z)


if __name__=="__main__":
    main()