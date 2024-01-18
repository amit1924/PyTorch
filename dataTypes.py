import torch

# 32 and 16 bit floating point is more common errors in pytorch
floatData = torch.tensor([3.1, 6.2])
print("floatData: ", floatData)
print("DataType: ", floatData.dtype)
float_16_bit_Data = floatData.type(torch.float16)
print("Convert into 16-bit:", float_16_bit_Data)

# Integer types
integerData = torch.tensor([3, 4])
print("Integer Data: ", integerData)
print("DataType: ", integerData.dtype)
# print("Multiplication of float and integer:", floatData * integerData)
print(f"Multiplication of float and integer: {floatData*integerData}")


# device
print("device tensor is on: ", integerData.device)
