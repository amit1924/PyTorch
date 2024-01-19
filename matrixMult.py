import torch

# Matrix multiplication
M1 = torch.tensor([[1, 2, 3], [2, 3, 4], [9, 8, 7]])

M2 = torch.tensor([[1, 2, 3], [2, 3, 4], [9, 8, 7]])

elem_multi = M1 * M2
print(f"Multiplication of matrix\n{elem_multi}")

# Another method
print("Inbuilt Method", torch.matmul(M1, M2))

# Shape errors are most common errors in the matrix multiplication


# Define matrices M3 and M4
M3 = torch.tensor([[1, 2]])  # Matrix with shape (1, 2)
M4 = torch.tensor([[7], [8]])  # Matrix with shape (2, 1)

# Check if the inner dimensions match
print(M4.shape[0])
if M3.shape[1] == M4.shape[0]:
    # Perform matrix multiplication
    mat_multi = torch.matmul(M3, M4)
    print(f"Matrix multiplication result:\n{mat_multi}")
else:
    print("Error: Inner dimensions do not match for matrix multiplication.")


# torch.mam=torch.matmul


# Transpose the matrix
M5 = torch.tensor([[7, 10], [9, 20], [15, 60]])
transpose = M5.T
print(f"Transposing Matrix:\n{transpose}")
print(f"Shape of M5 {M5.shape} dimensions")
print(f"Shape of transposed M5 {transpose.shape} dimensions")

print(f"Matrix multiplication result:\n{torch.matmul(M5, transpose)}")
print(
    f"Shape of Transpose Matrix after multiplication result shape in:\n{torch.matmul(M5, transpose).shape}"
)
