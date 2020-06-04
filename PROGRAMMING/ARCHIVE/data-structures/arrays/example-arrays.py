import numpy as np
from scipy import sparse
# vector row
vector_row = np.array([1,2,3])
# vector column
vector_column = np.array([[1],
			[2],
			[3]])

cars = ["Ford", "Volvo", "BMW"]

# Create a matrix
matrix = np.array([[1, 2],
                   [1, 2],
                   [1, 2]])


print(cars, "\n") 
print(vector_row, "\n") 
print(vector_column, "\n") 
print(matrix)

matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

# Create compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)
matrix[1,1]
