import torch

tensor = torch.tensor([1, 2, 3])
print(f"Addition:{tensor + 10}")
print(f"Subtraction:{tensor - 10}")
print(f"Multiplication:{tensor *10}")

print(f"Torch inbuilt Mult:{torch.mul(tensor, 100)}")
