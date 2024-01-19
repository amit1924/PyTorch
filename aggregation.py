import torch

x = torch.arange(0, 100, 10)
print(x)
# print(f"Type of x: {type (x)}")

# Minimum value
print(f"Minimum value: {x.min()}")

# maximum value
print(f"Maximum value: {x.max()}")

# Mean value
# print(f"Mean value: {x.mean()}")
# print(f"Data type of x: {x.dtype()}")

# convert x to float ,then only we can find mean
float_x = x.type(torch.float32)
print(f"Converting x to float:{float_x}")

print(f"Mean value: {float_x.mean()}")
