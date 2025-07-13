lis = [0, 1, 2, 3, 4, 5]
x = lis[:3]  # [0,1,2]
y = lis[-3:]  # [3,4,5]
print(x)
print(y)
lis = [i for i in lis if i % 2 != 0]
print(lis)
lis = lis + [0, 2, 4]
print(lis)

_tuple = (0, 1, 2)
print(_tuple[1])
_set = {5, 15, 8, 0, 34, 4}
print(_set, type(_set))
_dict = {
    "k": "v",
    "k1": "v1",
    "k2": "v2",
}
