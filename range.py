import torch

# Creating a range
range = torch.arange(1, 10)
print("Range: ", range)
print("Type of range:", type(range))


range = torch.arange(start=0, end=1000, step=50)
print("Range: ", range)

# Creating Tensors Like
tenZeroes = torch.zeros_like(input=range)
print(tenZeroes)
