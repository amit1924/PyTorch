import torch

x = torch.arange(0, 100, 10)
print(x)

# Find positional min and max values
print(f"at index 0:{x[0]}")
print(f"at index 1:{x[1]}")
print(f"Min value from argmin to find minimum index:{x.argmin()}")
print(f"Max value from argmax to find maximum index:{x.argmax()}")
