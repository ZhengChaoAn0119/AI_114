dic = {"Key_1": "Value_1", "Key_2": "Value_2"}
print(dic)
print(dic["Key_2"])

dic.update({"Key_3": "Value_3"})
print(dic)

del dic["Key_2"]
print(dic)


dic_2 = {x: x**2 for x in [1, 2, 3]}
print(dic_2)
