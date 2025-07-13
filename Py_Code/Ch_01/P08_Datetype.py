Bl = True
x = 10
print(type(Bl), Bl, type(x), x)
print(hex(id(Bl)), hex(id(x)))
print("---------------------")
tmp_1 = Bl
tmp_2 = x
print(type(tmp_1), tmp_1, type(tmp_2), tmp_2)
print(hex(id(tmp_1)), hex(id(tmp_2)))
print("---------------------")
Bl = False
x = 9.0
print(type(Bl), Bl, type(x), x)
print(hex(id(Bl)), hex(id(x)))
print("---------------------")

print(type(tmp_1), tmp_1, type(tmp_2), tmp_2)
print(hex(id(tmp_1)), hex(id(tmp_2)))
# 註解
