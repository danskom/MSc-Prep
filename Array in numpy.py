import numpy as np 

zero_d_second_array = np.array(42)

print(zero_d_second_array)

# a zero degree array is a scalar rank zero tensor

one_d_array = np.array([1,2,3,4,5,])

print(one_d_array)

# unidimensional array is a vector on rank one tensor

two_d_array = np.array([[1,2,3],[1,2,3]])

print (two_d_array)

# 2D array is a matrix a rank two tensor

three_d_array = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]] )

print (three_d_array)

