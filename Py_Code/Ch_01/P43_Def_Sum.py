import math


# def Sum(st, end):
#     return (st + end) * (end - st + 1) / 2


# st = float(input("Please input a start num: "))
# end = float(input("Please input a end num: "))
# S = Sum(st, end)
# print(S)


def GetArea(lenth=7, wihth=8):
    return lenth * wihth


def Circle(R=9):
    peri = 2 * math.pi * R
    area = math.pi * R**2
    return peri, area


print("default GetArea is ", f"{GetArea()}")
print("5*6 GetArea is ", f"{GetArea(5,6)}")

print(f"default Circle peri is {Circle()[0]:.2f}, area is {Circle()[1]:.2f}")
print(f"The R = 1 Circle peri is {Circle(1)[0]:.2f}, area is {Circle(1)[1]:.2f}")
