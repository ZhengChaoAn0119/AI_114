import numpy as np

x_0 = np.array([1, 2, 3])
x_1 = np.array([11, 22, 33])

x = np.array([x_0, x_1])
print(f"x_0 : {x_0}, type is : {type(x_0)}, nDim : {x_0.ndim}, shape : {x_0.shape}")
print(f"x : {x}, type is : {type(x)}, nDim : {x.ndim}, shape : {x.shape}")


for row in range(0, len(x)):  # x[0] x[1]
    for col in range(0, len(x[row])):  # x[0][] x[0][1] x[0][2]
        x[row][col] += 1  # 更改原本 index 的直
        print(x[row][col], end=", ")  # range() index
    print()
print(x)  # 被更改 x的值


x = np.array([x_0, x_1])
print(x)
for rowElements in x:
    for colElement in rowElements:
        colElement += 1  # 被更改的是 for 回圈內的變數 colElement 並不是原本x index的值
        print(colElement, end=", ")
    print()
print(x)
