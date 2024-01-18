import torch

# print("Pytorch Version:", torch.__version__)

# # Scalar
# scalar = torch.tensor(7)
# print("Scalar:", scalar)

# print(torch)
# print("Dimension:", scalar.ndim)


# # Vector
# vector = torch.tensor([7, 7])
# print("Vector:", vector)

# print("Dimension:", vector.ndim)
# print("Shape:", vector.shape)


# # Matrix
# Matrix = torch.tensor([[7, 8], [8, 9]])

# print("Matrix:", Matrix)
# print("Dimension:", Matrix.ndim)
# print("Shape:", Matrix.shape)


# # Tensor
# Tensor = torch.tensor([[7, 8, 10], [8, 9, 5], [10, 5, 6]])

# print("Tensor:", Tensor)
# print("Dimension:", Tensor.ndim)
# print("Shape:", Tensor.shape)
# print("Index:", Tensor[1, 2])
# print("Index:", Tensor[2, 2])
# print("At 0:", Tensor[0])


# Random Tensors
# This creates a 3x4 matrix (tensor) filled with random numbers between 0 and 1.
# randomTensor = torch.rand(3, 4)
# print("Random tensor:", randomTensor)
# print("dimension:", randomTensor.ndim)
# print("shape:", randomTensor.shape)


# randomTensor = torch.rand(1, 3, 4)
# print("Random tensor:", randomTensor)
# print("dimension:", randomTensor.ndim)


# Random Tensor Image
# randomImage = torch.rand(size=(224, 224, 3))
# print("Random image:", randomImage)
# print("dimension:", randomImage.ndim)
# print("shape:", randomImage.shape)
# zeros and ones
zero = torch.zeros(size=(3, 4))
print("zeros:", zero)

one = torch.ones(size=(3, 4))
print("one:", one)

print("Multiplication of ones and zeros:", one * zero)
