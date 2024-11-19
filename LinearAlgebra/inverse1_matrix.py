'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : inverse of matrix

'''
import numpy as np
 
def inv1_matrix(X):
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
    
    X = np.array([[12,7,3], [4 ,5,6], [7 ,8,9]]) 
    Z= inv1_matrix(X)
    print(Z)


if __name__=="__main__":
    main()